// Station sketch: reads the Grove sensors on the Base Shield, shows them on the
// 16x2 LCD and exposes the same readings as an NFC tag, so a phone tap shows
// the current data when the display is not readable.
//
// I2C (Wire): AHT20 0x38, LCD 0x3E. A0: light sensor. PN532 on the shield
// UART port (D0/D1 = Serial1), emulating a Type 4 tag from its own thread.

#include <Arduino_RouterBridge.h>
#include <Wire.h>
#include <Adafruit_AHTX0.h>
#include <rgb_lcd.h>
#include "pn532_tag.h"

constexpr uint32_t SENSOR_PERIOD_MS = 1000;
constexpr size_t NFC_STACK_SIZE = 1024;  // = CONFIG_DYNAMIC_THREAD_STACK_SIZE (pool slot)
constexpr int NFC_PRIORITY = 2;          // preempts loop() so taps are answered quickly

Adafruit_AHTX0 aht;
rgb_lcd lcd;
Pn532Tag tag(Serial1);

bool has_aht = false;
bool has_nfc = false;
static struct k_thread nfc_data;

static void nfc_thread(void*, void*, void*) {
  while (true) {
    tag.poll();
    k_msleep(1);
  }
}

void setup() {
  Bridge.begin();
  Monitor.begin();
  Wire.begin();

  has_aht = aht.begin(&Wire);
  lcd.begin(16, 2);

  has_nfc = tag.begin();
  if (has_nfc) {
    k_thread_stack_t* stack = k_thread_stack_alloc(NFC_STACK_SIZE, 0);
    if (stack == nullptr) {
      has_nfc = false;
    } else {
      k_tid_t tid = k_thread_create(&nfc_data, stack, NFC_STACK_SIZE, nfc_thread,
                                    nullptr, nullptr, nullptr, NFC_PRIORITY, 0, K_NO_WAIT);
      k_thread_name_set(tid, "nfc_tag");
    }
  }

  Monitor.print("station started: AHT20=");
  Monitor.print(has_aht ? "ok" : "missing");
  Monitor.print(" NFC=");
  Monitor.println(has_nfc ? "ok" : "missing");
}

void loop() {
  float temp_c = NAN;
  float hum_pct = NAN;
  if (has_aht) {
    sensors_event_t humidity, temp;
    aht.getEvent(&humidity, &temp);
    temp_c = temp.temperature;
    hum_pct = humidity.relative_humidity;
  }
  int light_raw = analogRead(A0);
  uint32_t uptime_s = millis() / 1000;

  char text[Pn532Tag::MAX_TEXT];
  snprintf(text, sizeof(text), "PoopVolt: T=%.1fC RH=%.0f%% light=%d up=%lus",
           (double)temp_c, (double)hum_pct, light_raw, (unsigned long)uptime_s);
  tag.setText(text);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(temp_c, 1);
  lcd.print("C ");
  lcd.print(hum_pct, 0);
  lcd.print("% L");
  lcd.print(light_raw);
  lcd.setCursor(0, 1);
  lcd.print(has_nfc ? "NFC: tap phone" : "NFC: missing");

  Monitor.print(text);
  Monitor.print(" nfc_reads=");
  Monitor.println(tag.reads());

  delay(SENSOR_PERIOD_MS);
}
