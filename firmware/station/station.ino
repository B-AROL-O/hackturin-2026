// Station sketch: reads the Grove sensors on the Base Shield, shows them on the
// 16x2 LCD, exposes the same readings as an NFC tag (a phone tap shows them when
// the display is not readable) and streams them to the Linux side over the
// Bridge as notify("station", seq, uptime_ms, temp_c, rh_pct, light_raw, pv_ma,
// pv_mv); see linux/station_rx.py.
//
// I2C (Wire): AHT20 0x38, LCD 0x3E. A0: light sensor. A1: Grove 2.5A DC current
// sensor (ACS70331) in series with the solar panel. PN532 on the shield
// UART port (D0/D1 = Serial1), emulating a Type 4 tag from its own thread.

#include <Arduino_RouterBridge.h>
#include <Wire.h>
#include <Adafruit_AHTX0.h>
#include <rgb_lcd.h>
#include "pn532_tag.h"

constexpr uint32_t SENSOR_PERIOD_MS = 1000;
constexpr float ADC_REF_MV = 3300.0f;      // 10-bit ADC, 3.3 V reference
constexpr float PV_ZERO_MV = 266.5f;       // sensor output at 0 A, measured in the dark 2026-10-10
constexpr float PV_MA_PER_MV = 1000.0f / 800.0f;  // ACS70331 module: 800 mV/A
constexpr size_t NFC_STACK_SIZE = 1024;  // = CONFIG_DYNAMIC_THREAD_STACK_SIZE (pool slot)
constexpr int NFC_PRIORITY = 2;          // preempts loop() so taps are answered quickly

Adafruit_AHTX0 aht;
rgb_lcd lcd;
Pn532Tag tag(Serial1);

bool has_aht = false;
bool has_nfc = false;
uint32_t seq = 0;
static struct k_thread nfc_data;

float read_pv_mv() {
  long sum = 0;
  for (int i = 0; i < 10; i++) {
    sum += analogRead(A1);
    delay(2);
  }
  return sum / 10.0f * ADC_REF_MV / 1024.0f;
}

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
  float pv_mv = read_pv_mv();
  float pv_ma = (pv_mv - PV_ZERO_MV) * PV_MA_PER_MV;
  uint32_t uptime_ms = millis();
  uint32_t uptime_s = uptime_ms / 1000;

  char text[Pn532Tag::MAX_TEXT];
  snprintf(text, sizeof(text), "PoopVolt: T=%.1fC RH=%.0f%% light=%d Ipv=%.0fmA up=%lus",
           (double)temp_c, (double)hum_pct, light_raw, (double)pv_ma, (unsigned long)uptime_s);
  tag.setText(text);
  Bridge.notify("station", seq++, uptime_ms, temp_c, hum_pct, light_raw, pv_ma, pv_mv);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(temp_c, 1);
  lcd.print("C ");
  lcd.print(hum_pct, 0);
  lcd.print("% L");
  lcd.print(light_raw);
  lcd.setCursor(0, 1);
  lcd.print("Ipv ");
  lcd.print(pv_ma, 0);
  lcd.print("mA");
  lcd.print(has_nfc ? " NFC" : "");

  Monitor.print(text);
  Monitor.print(" pv_mv=");
  Monitor.print(pv_mv, 1);
  Monitor.print(" nfc_reads=");
  Monitor.println(tag.reads());

  delay(SENSOR_PERIOD_MS);
}
