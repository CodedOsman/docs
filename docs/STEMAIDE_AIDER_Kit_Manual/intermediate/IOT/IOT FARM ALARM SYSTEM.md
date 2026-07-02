# Project 164
## IOT FARM ALERT SYSTEM

**Intermediate Embedded Systems Project Using Raspberry Pi Pico 2 W and MicroPython**

| Field | Value |
|-------|-------|
| Manual Section | Intermediate Projects |
| Project Level | Intermediate |
| Board | Raspberry Pi Pico 2 W |
| Programming Language | MicroPython |
| Version | 1.0 |
| Date | May 2026 |
| Prepared for | STEMAIDE Africa |

---

## Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Required Components](#required-components)
- [Before You Begin](#before-you-begin)
- [Circuit Connections](#circuit-connections)
- [Wiring Diagram](#wiring-diagram)
- [Step-by-Step Assembly](#step-by-step-assembly)
- [Testing Individual Components](#testing-individual-components)
- [Full Project Code](#full-project-code)
- [How the Code Works](#how-the-code-works)
- [Expected Result](#expected-result)
- [Troubleshooting](#troubleshooting)
- [Challenge Extensions](#challenge-extensions)
- [Reflection Questions](#reflection-questions)
- [Save Your Work](#save-your-work)
- [Next Project](#next-project)

---

## Overview

This project builds a farm alarm node that reacts to motion, dangerous temperature, and dangerous humidity conditions.

Students will connect a PIR motion sensor, a BME280 climate sensor, and an alarm output, then test how the Pico handles immediate and confirmed alert conditions.

The final system should sound a buzzer, light a warning LED, and report clear alarm messages through the Thonny Shell. In this classroom version, the serial monitor is the communication channel instead of a cloud service.

### Project Story

The real-world use case is a greenhouse, storage room, or protected farm area where staff need a fast warning when something unusual happens.

---

## Learning Objectives

- Combine motion sensing and environmental sensing in one alarm project
- Use confirmation logic to reduce false environmental alarms
- Trigger an audible alarm output safely from a Pico
- Use serial monitoring as a simple communication layer
- Think about alarm priorities and cooldown timing
- Describe an IoT-style alert system without overclaiming cloud features that are not implemented

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board | Use MicroPython firmware |
| PIR motion sensor | 1 | Detects movement in the monitored area | Use a 3.3V-compatible output or level shifting if required |
| BME280 sensor module | 1 | Temperature, humidity, and pressure input | Requires bme280.py on the Pico |
| Active buzzer | 1 | Audible alarm output | Use a buzzer that can be driven safely from the chosen interface |
| Red LED and 220 Ω resistor | 1 each | Visual alarm indicator | Always use a current-limiting resistor |
| Green LED and 220 Ω resistor | 1 each | System armed / normal indicator | Always use a current-limiting resistor |
| Breadboard and jumper wires | 1 | Temporary circuit wiring | Turn off power before rewiring |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- If needed, install the latest stable MicroPython firmware for the Pico / Pico 2 W before testing
- No external library is required. This project uses only built-in MicroPython modules
- Use `import os` and `print(os.listdir())` in the Thonny Shell to verify that the Pico file system is accessible

### Project-Specific Safety Note

Use a buzzer current that is safe for the Pico output or drive it through a transistor stage if the buzzer requires more current.

Keep wires secure because false motion or climate alarms are often caused by loose connections.

Test the buzzer volume carefully so it is loud enough to notice but not unsafe at close range.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| PIR VCC | Physical pin 36 | Physical pin 36 | Power connection if the sensor supports 3.3V |
| PIR OUT | GPIO 4 / physical pin 6 | GPIO 4 / physical pin 6 | Motion signal input |
| PIR GND | Any GND pin | Any GND pin | Common ground |
| Buzzer positive | GPIO 15 / physical pin 20 | GPIO 15 / physical pin 20 | Alarm output |
| Buzzer negative | Any GND pin | Any GND pin | Return path |
| Red LED anode | GPIO 16 through 220 Ω resistor | GPIO 16 / physical pin 21 | Alarm indicator |
| Green LED anode | GPIO 17 through 220 Ω resistor | GPIO 17 / physical pin 22 | Armed / normal indicator |
| Both LED cathodes | GND | Any GND pin | Return path for LEDs |
| BME280 VCC | 3.3V | Physical pin 36 | Sensor power |
| BME280 GND | GND | Any GND pin | Common ground |
| BME280 SDA | GPIO 2 | GPIO 2 / physical pin 4 | I2C data |
| BME280 SCL | GPIO 3 | GPIO 3 / physical pin 5 | I2C clock |

---

## Wiring Diagram

```
  Raspberry Pi Pico 2 W
  ┌─────────────────────┐
  │                     │
  │  GPIO 4  ───────────┤──── PIR OUT
  │                     │
  │  GPIO 2  ───────────┤──── BME280 SDA
  │  GPIO 3  ───────────┤──── BME280 SCL
  │                     │
  │  GPIO 15 ───────────┤──── Buzzer (+)
  │  GPIO 16 ────220Ω───┤──── Red LED (+)
  │  GPIO 17 ────220Ω───┤──── Green LED (+)
  │                     │
  │  3.3V    ───────────┤──── PIR VCC
  │  3.3V    ───────────┤──── BME280 VCC
  │                     │
  │  GND     ───────────┤──── PIR GND
  │  GND     ───────────┤──── Buzzer (-)
  │  GND     ───────────┤──── Red LED (-)
  │  GND     ───────────┤──── Green LED (-)
  │  GND     ───────────┤──── BME280 GND
  │                     │
  └─────────────────────┘
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W
Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Position the PIR Motion Sensor
Place the PIR motion sensor so it faces the protected farm area. Identify VCC, GND, and OUT before wiring.

### Step 3: Connect the PIR Sensor
Connect PIR VCC to 3.3V if your PIR module supports 3.3V operation. Connect PIR GND to GND. Connect PIR OUT to GPIO 4.

### Step 4: Place the BME280 Sensor Module
Place the BME280 module where it can sense the farm-area air. Connect BME280 VCC to 3.3V. Connect BME280 GND to GND. Connect BME280 SDA to GPIO 2 and BME280 SCL to GPIO 3. If you are using a bare BME280 sensor instead of a module, use the module pins labeled VCC, GND, SDA, and SCL to 3.3V.

### Step 5: Place and Connect the Buzzer
Place the buzzer on the breadboard and identify its positive (+) and negative (-) pins. Connect the buzzer positive pin to GPIO 15. Connect the buzzer negative pin to GND.

### Step 6: Place and Connect the Red LED
Place the red LED on the breadboard. Identify the long leg as the anode (+) and the short leg as the cathode (-). Connect the red LED long leg through a 220Ω resistor to GPIO 16. Connect the red LED short leg to GND.

### Step 7: Place and Connect the Green LED
Place the green LED on the breadboard. Identify the long leg as the anode (+) and the short leg as the cathode (-). Connect the green LED long leg through a 220Ω resistor to GPIO 17. Connect the green LED short leg to GND.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] PIR OUT connects to GPIO 4
- [x] BME280 SDA connects to GPIO 2 and SCL connects to GPIO 3
- [x] Buzzer positive pin connects to GPIO 15
- [x] Buzzer negative pin connects to GND
- [x] Red LED long leg connects through a 220Ω resistor to GPIO 16
- [x] Green LED long leg connects through a 220Ω resistor to GPIO 17
- [x] Both LED short legs connect to GND
- [x] All device grounds connect to Pico GND
- [x] No loose jumper wires

> **Intermediate Note**
> Allow the PIR sensor to warm up before testing alarms. The BME280 needs a short delay between readings, so do not expect instant climate updates.

> **Safety Note**
> Raspberry Pi Pico GPIO pins are 3.3V only. Use a 3.3V-safe PIR signal and keep the alarm buzzer to short classroom test bursts.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the PIR, BME280, buzzer, and LED wiring on a breadboard
- Give the PIR sensor time to stabilize after power-up before judging its motion behaviour

### Test the Input Sensor

- Read the PIR state while moving in front of it to confirm motion detection
- Read the BME280 temperature and humidity values several times to confirm stable climate readings

### Test the Output Device

- Run a short buzzer pulse test and confirm the red and green LEDs respond as expected
- If the buzzer is too quiet or too loud, check that the chosen device is appropriate for direct control

### Test Communication

- Open the Thonny Shell and confirm that the program prints normal-state messages and alarm reasons
- Check that the printed alarm reason matches the actual sensor event, such as motion or high humidity

### Run the Full System

- Trigger motion and then create a warm or humid condition so you can compare immediate and confirmed alarms
- Verify that the cooldown prevents the buzzer from sounding continuously every loop cycle

### Save the Project

- Save the final program and record the alarm thresholds used in your test area
- Note whether the PIR placement caused any false triggers so the sensor can be repositioned later

### Additional Testing and Calibration Checks

- **Motion test**: move in front of the PIR and confirm the alarm response
- **Normal condition test**: allow the system to sit in a stable room and verify it stays in the armed state
- **Threshold condition test**: create a warmer or more humid condition and confirm the environmental confirmation counter reaches the alarm state
- **Output response test**: confirm the buzzer, red LED, and green LED all match the reported system state
- **Calibration note**: if the PIR gives false triggers, adjust its position and allow enough warm-up time after powering it

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import I2C, Pin
import bme280
import time

pir = Pin(4, Pin.IN)
i2c_bme = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
bme = bme280.BME280(i2c=i2c_bme)


def number_from_bme(text_value):
    cleaned = "".join(ch for ch in str(text_value) if ch.isdigit() or ch in ".-")
    return float(cleaned)


def read_bme280():
    temp_text, pressure_text, humidity_text = bme.values
    return number_from_bme(temp_text), number_from_bme(humidity_text), number_from_bme(pressure_text)


buzzer = Pin(15, Pin.OUT)
red_led = Pin(16, Pin.OUT)
green_led = Pin(17, Pin.OUT)

TEMP_ALERT = 35
HUMIDITY_ALERT = 90
ENV_CONFIRMATIONS = 2
ALARM_COOLDOWN = 10

buzzer.value(0)
red_led.value(0)
green_led.value(1)
last_alarm_time = time.time() - ALARM_COOLDOWN
high_temp_hits = 0
high_humidity_hits = 0


def alarm(reason):
    global last_alarm_time
    print('ALARM:', reason)
    red_led.value(1)
    green_led.value(0)
    for _ in range(4):
        buzzer.value(1)
        time.sleep(0.15)
        buzzer.value(0)
        time.sleep(0.15)
    last_alarm_time = time.time()


print('=== IoT Farm Alarm System ===')
print('Serial output is the communication channel in this classroom version.\n')

while True:
    motion_detected = pir.value() == 1
    sensor_error = None
    temp_c = None
    humidity = None

    try:
        temp_c, humidity, pressure_hpa = read_bme280()
    except Exception as error:
        sensor_error = error

    if temp_c is not None and temp_c >= TEMP_ALERT:
        high_temp_hits += 1
    else:
        high_temp_hits = 0

    if humidity is not None and humidity >= HUMIDITY_ALERT:
        high_humidity_hits += 1
    else:
        high_humidity_hits = 0

    reasons = []
    if motion_detected:
        reasons.append('motion detected')
    if high_temp_hits >= ENV_CONFIRMATIONS:
        reasons.append('temperature above {} C'.format(TEMP_ALERT))
    if high_humidity_hits >= ENV_CONFIRMATIONS:
        reasons.append('humidity above {} %'.format(HUMIDITY_ALERT))

    now = time.time()
    if reasons and (now - last_alarm_time) >= ALARM_COOLDOWN:
        alarm(', '.join(reasons))
    else:
        if not reasons:
            red_led.value(0)
            green_led.value(1)
        print('Motion: {} | Temp: {} C | Humidity: {} % | Temp hits: {} | Humidity hits: {}'.format(
            motion_detected, temp_c, humidity, high_temp_hits, high_humidity_hits
        ))
        if sensor_error is not None:
            print('Sensor read error:', sensor_error)

    time.sleep(2)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| ENV_CONFIRMATIONS | Counts consecutive high readings before triggering | This reduces false alarms from one unstable reading |
| Motion alarm rule | Fires immediately on any motion detection | Security-related events usually need a faster response |
| ALARM_COOLDOWN | Prevents repeated alarms for a set time | Makes the system easier to live with during testing |
| Serial log output | Prints status and alarm events to the Shell | Acts like a simple event log for an IoT-style prototype |

---

## Expected Result

When no alert condition is active, the green LED should stay on and the Shell should print normal status messages.

When the PIR detects motion, the buzzer should sound, the red LED should turn on, and the Shell should report a motion alarm.

When temperature or humidity stays above the alert threshold for repeated readings, the system should trigger the alarm and report the specific environmental cause.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The PIR triggers when nobody moves | Sensor needs stabilization or is near drafts | Wait for stabilization and point the sensor away from direct drafts, windows, or heaters |
| The buzzer never sounds | Buzzer type or wiring issue | Use an active buzzer or add a suitable driver stage if needed |
| The system alarms too often for climate changes | Thresholds too sensitive or confirmations too low | Increase the thresholds or keep ENV_CONFIRMATIONS at 2 or more |
| The Shell shows sensor errors | BME280 wiring or timing issue | Check the GPIO 2/3 wiring and keep enough delay between reads |

---

## Challenge Extensions

- Add Wi-Fi or BLE notification support as a later communication upgrade
- Add a second buzzer pattern so motion and climate alarms sound different
- Add a manual arm/disarm button for maintenance periods
- Add a log file or dashboard so alarm events can be reviewed later

---

## Reflection Questions

1. Why should motion alarms usually react faster than temperature or humidity alarms?
2. Why is a cooldown useful in an alarm system?
3. What is the difference between an IoT-ready alarm node and a full cloud-connected alarm system?
4. What would you improve before installing this in a real farm building?

---

## Save Your Work

Save the file to your computer as:

```
project_164_iot_farm_alarm_system.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 165: Smart Irrigation Failure Detection**