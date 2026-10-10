// Minimal PN532 driver over HSU (UART) that emulates an NFC Forum Type 4 tag
// holding one NDEF Text record. A phone tapping the reader sees a read-only
// tag with the current text (Android reads it natively, e.g. with NFC Tools).
//
// poll() never blocks for long: call it often, ideally from its own thread.
// setText() may be called from another thread.

#pragma once

#include <Arduino.h>

class Pn532Tag {
 public:
  static constexpr size_t MAX_TEXT = 100;

  explicit Pn532Tag(HardwareSerial& serial) : serial_port(serial) {}

  bool begin();  // wake up + configure; false if no PN532 answers
  uint32_t firmwareVersion() const { return fw_version; }
  void setText(const char* text);
  void poll();
  uint32_t reads() const { return ndef_reads; }

 private:
  enum class State { Idle, WaitActivation, WaitGetData, WaitSetData };

  void send(const uint8_t* cmd, uint8_t len);
  bool readFrame();
  bool command(const uint8_t* cmd, uint8_t len, uint32_t timeout_ms);
  void startEmulation();
  void handleApdu(const uint8_t* apdu, uint8_t len);
  void consume(size_t n);

  HardwareSerial& serial_port;
  uint32_t fw_version = 0;
  State state = State::Idle;
  uint32_t state_since = 0;
  uint32_t ndef_reads = 0;

  uint8_t rx[128];
  size_t rx_len = 0;
  uint8_t frame[128];  // last received frame: TFI, response code, data
  uint8_t frame_len = 0;

  enum class File { None, Cc, Ndef } selected = File::None;
  bool app_selected = false;
  struct k_mutex ndef_mutex;
  uint8_t ndef_file[2 + 7 + MAX_TEXT];  // NLEN + NDEF message
  size_t ndef_file_len = 0;
};
