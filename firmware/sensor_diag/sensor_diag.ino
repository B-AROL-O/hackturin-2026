// Sensor diagnostic for the UNO Q + Seeed Grove Base Shield (VCC switch at 3.3V).
//
// I2C (header SDA/SCL = Wire): AHT20 0x38, Grove 16x2 LCD 0x3E (+ RGB backlight
// 0x62 or 0x30 on the RGB version), PN532 NFC 0x24. Analog A0: Grove light sensor.
// Scans the bus (again every 5 s while the PN532 is missing), then every second reads each detected device, prints to
// the Monitor and shows the readings on the LCD.

#include <Arduino_RouterBridge.h>
#include <Wire.h>
#include <Adafruit_AHTX0.h>
#include <Adafruit_PN532.h>
#include <rgb_lcd.h>

constexpr uint8_t ADDR_AHT20 = 0x38;
constexpr uint8_t ADDR_LCD = 0x3E;
constexpr uint8_t ADDR_LCD_RGB = 0x62;
constexpr uint8_t ADDR_LCD_RGB_V5 = 0x30;
constexpr uint8_t ADDR_PN532 = 0x24;
constexpr uint8_t NO_PIN = 0xFF;  // Grove NFC does not wire IRQ/RESET

Adafruit_AHTX0 aht;
Adafruit_PN532* nfc = nullptr;  // created in setup(): its constructor touches pins and the heap
rgb_lcd lcd;

bool has_aht = false;
bool has_lcd = false;
bool has_nfc = false;

bool probe(uint8_t addr) {
  Wire.beginTransmission(addr);
  return Wire.endTransmission() == 0;
}

void scan() {
  Monitor.println("I2C scan (Wire):");
  int found = 0;
  for (uint8_t addr = 0x08; addr < 0x78; addr++) {
    if (!probe(addr)) continue;
    found++;
    Monitor.print("  0x");
    Monitor.print(addr, HEX);
    switch (addr) {
      case ADDR_AHT20: Monitor.println(" AHT20"); break;
      case ADDR_LCD: Monitor.println(" LCD controller"); break;
      case ADDR_LCD_RGB:
      case ADDR_LCD_RGB_V5: Monitor.println(" LCD RGB backlight"); break;
      case ADDR_PN532: Monitor.println(" PN532"); break;
      default: Monitor.println(" unknown"); break;
    }
  }
  if (found == 0) Monitor.println("  nothing found: check shield seating and the 3.3V/5V switch");
}

void init_nfc() {
  if (probe(ADDR_PN532)) {
    if (nfc == nullptr) nfc = new Adafruit_PN532(NO_PIN, NO_PIN, &Wire);
    nfc->begin();
    uint32_t version = nfc->getFirmwareVersion();
    if (version) {
      nfc->SAMConfig();
      has_nfc = true;
      Monitor.print("PN532: OK, firmware ");
      Monitor.print((version >> 16) & 0xFF);
      Monitor.print(".");
      Monitor.println((version >> 8) & 0xFF);
    } else {
      Monitor.println("PN532: ACKs at 0x24 but no firmware reply");
    }
  } else {
    Monitor.println("PN532: not found at 0x24 (is the module set to I2C, not UART?)");
  }
}

void setup() {
  Bridge.begin();
  Monitor.begin();
  delay(2000);  // let the Monitor connect before the scan output
  Monitor.println("sensor_diag boot");

  Wire.begin();
  Monitor.println("Wire started");
  scan();

  has_aht = aht.begin(&Wire);
  Monitor.println(has_aht ? "AHT20: OK" : "AHT20: not responding");

  if (probe(ADDR_LCD)) {
    lcd.begin(16, 2);
    lcd.setRGB(0, 64, 128);
    lcd.print("sensor_diag");
    has_lcd = true;
    Monitor.println("LCD: OK");
  } else {
    Monitor.println("LCD: not found at 0x3E");
  }

  init_nfc();
}

void loop() {
  static uint32_t last_retry = 0;
  if (!has_nfc && millis() - last_retry > 5000) {  // keep looking while the NFC wiring is fixed
    last_retry = millis();
    scan();
    init_nfc();
  }

  float temp_c = NAN;
  float hum_pct = NAN;
  if (has_aht) {
    sensors_event_t humidity, temp;
    aht.getEvent(&humidity, &temp);
    temp_c = temp.temperature;
    hum_pct = humidity.relative_humidity;
  }

  int light_raw = analogRead(A0);  // 10-bit, 0..1023 over 0..3.3V

  String uid_hex;
  if (has_nfc) {
    uint8_t uid[7];
    uint8_t uid_len = 0;
    if (nfc->readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uid_len, 100)) {
      for (uint8_t i = 0; i < uid_len; i++) {
        if (uid[i] < 0x10) uid_hex += "0";
        uid_hex += String(uid[i], HEX);
      }
    }
  }

  Monitor.print("T=");
  Monitor.print(temp_c, 1);
  Monitor.print("C RH=");
  Monitor.print(hum_pct, 1);
  Monitor.print("% light=");
  Monitor.print(light_raw);
  Monitor.print(" nfc=");
  Monitor.println(uid_hex.length() ? uid_hex : "-");

  if (has_lcd) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(temp_c, 1);
    lcd.print("C ");
    lcd.print(hum_pct, 0);
    lcd.print("% L");
    lcd.print(light_raw);
    lcd.setCursor(0, 1);
    lcd.print(uid_hex.length() ? uid_hex : "no card");
  }

  delay(1000);
}
