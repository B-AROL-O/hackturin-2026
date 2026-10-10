// MCU side of the IMU -> Linux bridge (Arduino UNO Q, STM32U585 / Zephyr).
//
// A k_timer fires at SAMPLE_HZ and gives a semaphore from ISR context; the
// sampler thread blocks on it, reads the Modulino Movement (LSM6DSOX on the
// Qwiic connector, Wire1) and pushes the sample to Linux with
// Bridge.notify("imu", seq, t_us, ax, ay, az, gx, gy, gz).
// Units: acceleration in g, angular rate in dps, t_us = MCU uptime.

#include <Arduino_RouterBridge.h>
#include <Modulino.h>

constexpr uint32_t SAMPLE_HZ = 100;
constexpr size_t SAMPLER_STACK_SIZE = 1024;  // = CONFIG_DYNAMIC_THREAD_STACK_SIZE (pool slot)
constexpr int SAMPLER_PRIORITY = 2;  // preempts the Bridge update thread (5)

ModulinoMovement movement;

static struct k_timer tick_timer;
static struct k_sem tick_sem;
static struct k_thread sampler_data;
static k_thread_stack_t* sampler_stack;
static volatile uint32_t sent = 0;
static volatile uint32_t read_errors = 0;

static void on_tick(struct k_timer*) {
  k_sem_give(&tick_sem);  // limit 1: a late sampler skips ticks instead of bursting
}

static void sampler(void*, void*, void*) {
  uint32_t seq = 0;
  while (true) {
    k_sem_take(&tick_sem, K_FOREVER);
    uint64_t t_us = k_ticks_to_us_floor64(k_uptime_ticks());
    if (!movement.update()) {
      read_errors++;
      continue;
    }
    Bridge.notify("imu", seq++, t_us,
                  movement.getX(), movement.getY(), movement.getZ(),
                  movement.getRoll(), movement.getPitch(), movement.getYaw());
    sent++;
  }
}

void setup() {
  Bridge.begin();
  Monitor.begin();

  Modulino.begin();  // Wire1 = Qwiic on UNO Q
  while (!movement.begin()) {
    Monitor.println("Modulino Movement not found, retrying...");
    delay(1000);
  }

  k_sem_init(&tick_sem, 0, 1);
  k_timer_init(&tick_timer, on_tick, nullptr);

  sampler_stack = k_thread_stack_alloc(SAMPLER_STACK_SIZE, 0);
  if (sampler_stack == nullptr) {
    while (true) {
      Monitor.println("sampler stack alloc failed");
      delay(1000);
    }
  }
  k_tid_t tid = k_thread_create(&sampler_data, sampler_stack, SAMPLER_STACK_SIZE,
                                sampler, nullptr, nullptr, nullptr,
                                SAMPLER_PRIORITY, 0, K_NO_WAIT);
  k_thread_name_set(tid, "imu_sampler");

  k_timer_start(&tick_timer, K_USEC(1000000 / SAMPLE_HZ), K_USEC(1000000 / SAMPLE_HZ));
  Monitor.println("imu_bridge started");
}

void loop() {
  // Heartbeat on the Monitor (laptop: /dev/ttyACM0 or `arduino-cli monitor`).
  static uint32_t last_sent = 0;
  delay(5000);
  uint32_t now_sent = sent;
  Monitor.print("imu sent/5s=");
  Monitor.print(now_sent - last_sent);
  Monitor.print(" read_errors=");
  Monitor.println(read_errors);
  last_sent = now_sent;
}
