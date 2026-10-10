#include "pn532_tag.h"

// PN532 commands (PN532 User Manual, ch. 7).
constexpr uint8_t CMD_GET_FIRMWARE_VERSION = 0x02;
constexpr uint8_t CMD_SET_PARAMETERS = 0x12;
constexpr uint8_t CMD_SAM_CONFIGURATION = 0x14;
constexpr uint8_t CMD_TG_INIT_AS_TARGET = 0x8C;
constexpr uint8_t CMD_TG_GET_DATA = 0x86;
constexpr uint8_t CMD_TG_SET_DATA = 0x8E;
constexpr uint8_t TFI_HOST = 0xD4;
constexpr uint8_t TFI_PN532 = 0xD5;

constexpr uint32_t EXCHANGE_TIMEOUT_MS = 1000;

// Type 4 Tag capability container: mapping v2.0, MLe 0x3B, MLc 0x34, NDEF file
// E104 of up to sizeof(ndef_file) bytes, read free, write denied.
static const uint8_t NDEF_AID[] = {0xD2, 0x76, 0x00, 0x00, 0x85, 0x01, 0x01};
static const uint8_t CC_FILE[] = {0x00,
                                  0x0F,
                                  0x20,
                                  0x00,
                                  0x3B,
                                  0x00,
                                  0x34,
                                  0x04,
                                  0x06,
                                  0xE1,
                                  0x04,
                                  0x00,
                                  2 + 7 + Pn532Tag::MAX_TEXT,
                                  0x00,
                                  0xFF};

bool Pn532Tag::begin() {
  k_mutex_init(&ndef_mutex);
  setText("");

  ser.begin(115200);
  static const uint8_t wakeup[] = {0x55, 0x55, 0x00, 0x00, 0x00, 0x00,
                                   0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                   0x00, 0x00, 0x00, 0x00};
  ser.write(wakeup, sizeof(wakeup));
  delay(10);
  while (ser.available()) ser.read();

  const uint8_t sam[] = {CMD_SAM_CONFIGURATION, 0x01, 0x14,
                         0x01};  // normal mode
  if (!command(sam, sizeof(sam), 500)) return false;

  const uint8_t ver[] = {CMD_GET_FIRMWARE_VERSION};
  if (!command(ver, sizeof(ver), 500) || frame_len < 6) return false;
  fw_version = static_cast<uint32_t>(frame[2]) << 24 |
               static_cast<uint32_t>(frame[3]) << 16 |
               static_cast<uint32_t>(frame[4]) << 8 | frame[5];

  // fAutomaticATR_RES | fISO14443-4_PICC: the PN532 handles RATS/ATS itself.
  const uint8_t params[] = {CMD_SET_PARAMETERS, 0x24};
  if (!command(params, sizeof(params), 500)) return false;

  state = State::Idle;
  return true;
}

void Pn532Tag::setText(const char* text) {
  size_t n = strnlen(text, MAX_TEXT);
  k_mutex_lock(&ndef_mutex, K_FOREVER);
  uint8_t* p = ndef_file;
  size_t msg_len = 7 + n;
  *p++ = 0x00;
  *p++ = (uint8_t)msg_len;  // NLEN
  *p++ = 0xD1;              // MB | ME | SR | TNF=well-known
  *p++ = 0x01;              // type length
  *p++ = (uint8_t)(3 + n);  // payload length
  *p++ = 'T';               // Text record
  *p++ = 0x02;              // UTF-8, language code length 2
  *p++ = 'e';
  *p++ = 'n';
  memcpy(p, text, n);
  ndef_file_len = 2 + msg_len;
  k_mutex_unlock(&ndef_mutex);
}

void Pn532Tag::poll() {
  bool got = readFrame();
  bool is_error = got && frame[0] != TFI_PN532;

  switch (state) {
    case State::Idle:
      startEmulation();
      break;

    case State::WaitActivation:  // completes when a phone enters the field
      if (got) {
        if (is_error) {
          state = State::Idle;
          break;
        }
        app_selected = false;
        selected = File::None;
        const uint8_t get[] = {CMD_TG_GET_DATA};
        send(get, sizeof(get));
        state = State::WaitGetData;
        state_since = millis();
      }
      break;

    case State::WaitGetData:
      if (got) {
        if (is_error || frame_len < 3 ||
            frame[2] != 0x00) {  // status != OK: phone left
          state = State::Idle;
          break;
        }
        handleApdu(frame + 3, frame_len - 3);
        state = State::WaitSetData;
        state_since = millis();
      } else if (millis() - state_since > EXCHANGE_TIMEOUT_MS) {
        state = State::Idle;
      }
      break;

    case State::WaitSetData:
      if (got) {
        if (is_error || frame_len < 3 || frame[2] != 0x00) {
          state = State::Idle;
          break;
        }
        const uint8_t get[] = {CMD_TG_GET_DATA};
        send(get, sizeof(get));
        state = State::WaitGetData;
        state_since = millis();
      } else if (millis() - state_since > EXCHANGE_TIMEOUT_MS) {
        state = State::Idle;
      }
      break;
  }
}

void Pn532Tag::startEmulation() {
  // PICC-only, passive-only target; ISO14443-4 capable (SEL_RES 0x20).
  uint8_t cmd[1 + 1 + 6 + 18 + 10 + 2] = {};
  cmd[0] = CMD_TG_INIT_AS_TARGET;
  cmd[1] = 0x05;  // PassiveOnly | PICCOnly
  cmd[2] = 0x04;
  cmd[3] = 0x00;  // SENS_RES
  cmd[4] = 0x12;
  cmd[5] = 0x34;
  cmd[6] = 0x56;  // NFCID1t
  cmd[7] = 0x20;  // SEL_RES: ISO/IEC 14443-4
  // FeliCa params, NFCID3t, LEN Gt = 0, LEN Tk = 0: all zero.
  send(cmd, sizeof(cmd));
  state = State::WaitActivation;
}

void Pn532Tag::handleApdu(const uint8_t* apdu, uint8_t len) {
  uint8_t out[1 + 64];
  uint8_t n = 0;
  out[n++] = CMD_TG_SET_DATA;
  auto sw = [&](uint8_t sw1, uint8_t sw2) {
    out[n++] = sw1;
    out[n++] = sw2;
  };

  if (len < 4) {
    sw(0x67, 0x00);              // wrong length
  } else if (apdu[1] == 0xA4) {  // SELECT
    uint8_t lc = len > 4 ? apdu[4] : 0;
    const uint8_t* data = apdu + 5;
    if (apdu[2] == 0x04 && lc == sizeof(NDEF_AID) &&
        memcmp(data, NDEF_AID, lc) == 0) {
      app_selected = true;
      sw(0x90, 0x00);
    } else if (apdu[2] == 0x00 && app_selected && lc == 2 && data[0] == 0xE1 &&
               data[1] == 0x03) {
      selected = File::Cc;
      sw(0x90, 0x00);
    } else if (apdu[2] == 0x00 && app_selected && lc == 2 && data[0] == 0xE1 &&
               data[1] == 0x04) {
      selected = File::Ndef;
      sw(0x90, 0x00);
    } else {
      sw(0x6A, 0x82);  // file or application not found
    }
  } else if (apdu[1] == 0xB0) {  // READ BINARY
    size_t offset = static_cast<size_t>(apdu[2]) << 8 | apdu[3];
    size_t le = len > 4 ? apdu[4] : 0;
    if (le == 0 || le > 0x3B) le = 0x3B;  // MLe from the CC file
    if (selected == File::Cc && offset <= sizeof(CC_FILE)) {
      size_t count = min(
          le, sizeof(CC_FILE) - offset);  // NOLINT(build/include_what_you_use)
      memcpy(out + n, CC_FILE + offset, count);
      n += count;
      sw(0x90, 0x00);
    } else if (selected == File::Ndef) {
      k_mutex_lock(&ndef_mutex, K_FOREVER);
      if (offset <= ndef_file_len) {
        size_t count = min(
            le, ndef_file_len - offset);  // NOLINT(build/include_what_you_use)
        memcpy(out + n, ndef_file + offset, count);
        n += count;
        if (offset + count >= ndef_file_len) ndef_reads++;
        sw(0x90, 0x00);
      } else {
        sw(0x6B, 0x00);  // offset outside the file
      }
      k_mutex_unlock(&ndef_mutex);
    } else {
      sw(0x69, 0x86);  // no file selected
    }
  } else if (apdu[1] == 0xD6) {  // UPDATE BINARY
    sw(0x69, 0x82);              // read-only tag
  } else {
    sw(0x6D, 0x00);  // instruction not supported
  }
  send(out, n);
}

void Pn532Tag::send(const uint8_t* cmd, uint8_t len) {
  uint8_t frame_len_byte = len + 1;  // TFI + command
  uint8_t sum = TFI_HOST;
  for (uint8_t i = 0; i < len; i++) sum += cmd[i];
  const uint8_t header[] = {
      0x00,    0x00, 0xFF, frame_len_byte, (uint8_t)(0x100 - frame_len_byte),
      TFI_HOST};
  const uint8_t trailer[] = {(uint8_t)(0x100 - sum), 0x00};
  ser.write(header, sizeof(header));
  ser.write(cmd, len);
  ser.write(trailer, sizeof(trailer));
}

void Pn532Tag::consume(size_t n) {
  if (n >= rx_len) {
    rx_len = 0;
    return;
  }
  memmove(rx, rx + n, rx_len - n);
  rx_len -= n;
}

// Parses at most one information frame from the UART into `frame`; skips ACKs.
bool Pn532Tag::readFrame() {
  while (ser.available() && rx_len < sizeof(rx)) rx[rx_len++] = ser.read();

  while (true) {
    while (rx_len >= 3 && !(rx[0] == 0x00 && rx[1] == 0x00 && rx[2] == 0xFF))
      consume(1);
    if (rx_len < 5) return false;
    uint8_t len = rx[3];
    uint8_t lcs = rx[4];
    if ((len == 0x00 && lcs == 0xFF) ||
        (len == 0xFF && lcs == 0x00)) {  // ACK / NACK
      consume(5);
      continue;
    }
    if ((uint8_t)(len + lcs) != 0 || len > sizeof(frame)) {
      consume(1);
      continue;
    }
    if (rx_len < 5u + len + 1) return false;
    uint8_t sum = 0;
    for (uint8_t i = 0; i < len; i++) sum += rx[5 + i];
    if ((uint8_t)(sum + rx[5 + len]) != 0) {
      consume(1);
      continue;
    }
    memcpy(frame, rx + 5, len);
    frame_len = len;
    consume(5 + len + 1);
    return true;
  }
}

bool Pn532Tag::command(const uint8_t* cmd, uint8_t len, uint32_t timeout_ms) {
  send(cmd, len);
  uint32_t start = millis();
  while (millis() - start < timeout_ms) {
    if (readFrame())
      return frame[0] == TFI_PN532 && frame_len >= 2 && frame[1] == cmd[0] + 1;
    delay(1);
  }
  return false;
}
