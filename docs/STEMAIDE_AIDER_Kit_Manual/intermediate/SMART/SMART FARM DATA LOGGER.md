# Project 151
## SMART FARM DATA LOGGER

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
- [Wiring Check](#wiring-check)
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

The real-world use case is a monitoring trial where soil, climate, and rain state should be logged and exported later for spreadsheet analysis.

Students will combine soil, BME280, and rain-sensor inputs into one CSV logger with a visible write indicator.

The final system should create a log file, append timestamped records at a fixed interval, and make the stored data easy to inspect and export.

### Project Story

This project records several farm measurements over time so students can analyse environmental patterns instead of only watching live values.

---

## Learning Objectives

- Create and append structured CSV records in MicroPython
- Log several sensor readings in one row instead of separate files
- Use elapsed time when a real-time clock is not available
- Blink a status LED to confirm successful file writes
- Prepare farm data for later charting or comparison in a spreadsheet

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|---|---|---|---|
| Raspberry Pi Pico 2 W | 1 | Main controller | Use MicroPython |
| Soil moisture sensor | 1 | Analog moisture input | Calibrate before final logging |
| BME280 sensor module | 1 | Temperature, humidity, and pressure input | Requires bme280.py on the Pico |
| Rain sensor module | 1 | Digital rainfall input | Confirm the output is 3.3V safe |
| LED and 220Ω resistor | 1 each | Log-write indicator | Current-limited output only |
| Breadboard and jumper wires | 1 | Prototype wiring | Keep the sensor wiring stable |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- Software Installation and Setup
- Safety Guidelines
- Breadboard Basics
- Reading Circuit Diagrams

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules
- After the project runs, use `import os; print(os.listdir())` in Thonny to confirm that `farm_data_log.csv` was created on the Pico

### Project-Specific Safety Note

Do not remove power while the file is being written if you can avoid it.
Export important log files to your computer after testing instead of keeping the only copy on the board.
Keep water used for rain-sensor testing away from the Pico and USB cable.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---|---|---|---|
| Soil sensor AOUT | GPIO 26 | GPIO 26 / physical pin 31 | ADC moisture input |
| BME280 SDA | GPIO 2 | GPIO 2 / physical pin 4 | I2C data |
| BME280 SCL | GPIO 3 | GPIO 3 / physical pin 5 | I2C clock |
| BME280 VCC | 3.3V | Physical pin 36 | Sensor power |
| BME280 GND | GND | Any GND pin | Common ground |
| Rain sensor DOUT | GPIO 5 | GPIO 5 / physical pin 7 | Digital rain input |
| Status LED anode | GPIO 16 through 220Ω resistor | GPIO 16 / physical pin 21 | Blinks on successful log write |
| Status LED cathode | GND | Any GND pin | LED return |

---

## Wiring Diagram

![Circuit Diagram](../../assets/intermidiate/SMART/SMART FARM DATA LOGGER/circuit_1.png)

```text
Raspberry Pi Pico 2 W
┌─────────────────────┐
│                     │
│  GPIO 26 ───────────┼──── Soil sensor AOUT
│  GPIO 2  ───────────┼──── BME280 SDA
│  GPIO 3  ───────────┼──── BME280 SCL
│  3.3V    ───────────┼──── BME280 VCC / Soil VCC
│  GND     ───────────┼──── BME280 GND / Soil GND / LED cathode
│  GPIO 5  ───────────┼──── Rain sensor DOUT
│  GPIO 16 ───────────┼──── Resistor (220Ω) ── LED anode (+)
│                     │
└─────────────────────┘

BME280
VCC  ─────────────── 3.3V
GND  ─────────────── GND
SDA  ─────────────── GPIO 2
SCL  ─────────────── GPIO 3

Soil Sensor
VCC  ─────────────── 3.3V
GND  ─────────────── GND
AOUT ─────────────── GPIO 26

Rain Sensor
VCC  ─────────────── 3.3V
GND  ─────────────── GND
DOUT ─────────────── GPIO 5

Status LED
Anode (+) ──[220Ω]── GPIO 16
Cathode (-) ───────── GND
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W

Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Position the Soil Moisture Sensor

Place the soil moisture probe so the sensing end can enter the soil sample. Identify VCC, GND, and AOUT / AO / Signal before wiring.

### Step 3: Connect the Soil Sensor

Connect soil sensor VCC to 3.3V. Connect soil sensor GND to GND. Connect soil sensor AOUT, AO, or Signal to GPIO 26 (ADC0).

### Step 4: Place the BME280 Sensor Module

Identify BME280 VCC, GND, SDA, and SCL before wiring. Connect BME280 VCC to 3.3V. Connect BME280 GND to GND. Connect BME280 SDA to GPIO 2 and BME280 SCL to GPIO 3. If you are using a bare BME280 sensor, use the module pins labeled VCC, GND, SDA, and SCL.

### Step 5: Position and Connect the Rain Sensor

Place the rain sensor where test drops cannot drip onto the Pico or breadboard. Connect rain sensor VCC to 3.3V when the module supports 3.3V operation. Connect rain sensor GND to GND. Connect rain sensor DOUT to GPIO 5. Confirm the DOUT signal is safe for 3.3V Pico GPIO.

### Step 6: Place and Connect the Status LED

Place the status LED on the breadboard. Identify the long leg as the anode (+) and the short leg as the cathode (-). Connect the status LED long leg through a 220Ω resistor to GPIO 16. Connect the status LED short leg to GND.

---

## Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Soil sensor AOUT / AO / Signal connects to GPIO 26
- [x] BME280 SDA connects to GPIO 2 and SCL connects to GPIO 3
- [x] Rain sensor DOUT connects to GPIO 5
- [x] Rain sensor output is confirmed 3.3V-safe
- [x] Status LED long leg connects through a 220Ω resistor to GPIO 16
- [x] Status LED short leg connects to GND
- [x] No loose jumper wires

> **Intermediate Note**
>
> Confirm that all sensor readings look believable before logging repeatedly. The BME280 needs a short delay between readings, and the rain sensor should be tested dry and wet.

> **Safety Note**
>
> Keep water drops away from the Pico, breadboard, USB cable, and jumper wires. Avoid removing power while a log entry is actively being written.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware setup

- Build the three sensor circuits and the status LED before running the full logger
- Keep the log setup simple at first so you can verify one CSV file path only

### Test the input sensors

- Calibrate the soil sensor and test the BME280 and rain sensor individually
- Confirm that all readings look believable before writing them to a file repeatedly

### Test the output data

- Run the logger long enough to create several CSV rows
- Watch the status LED blink each time a row is written

### Run the full system

- Open the CSV file in Thonny after a few logging intervals to confirm the structure
- Export the file to your computer and view it in a spreadsheet if possible

### Save the project

- Save the final code and export the CSV file for later analysis
- Record the log interval used in your final test

### Quick testing checklist

- ☐ `farm_data_log.csv` appears in `os.listdir()`
- ☐ New rows are appended at the chosen interval
- ☐ The status LED blinks during successful writes
- ☐ Each row contains moisture, temperature, humidity, and rain data
- ☐ The file can be exported and opened for later analysis

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, I2C, Pin
import bme280
import os
import time

soil = ADC(26)
i2c_bme = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
bme = bme280.BME280(i2c=i2c_bme)

def number_from_bme(text_value):
    cleaned = "".join(ch for ch in str(text_value) if ch.isdigit() or ch in ".-")
    return float(cleaned)

def read_bme280():
    temp_text, pressure_text, humidity_text = bme.values
    return number_from_bme(temp_text), number_from_bme(humidity_text), number_from_bme(pressure_text)

rain_sensor = Pin(5, Pin.IN, Pin.PULL_UP)
status_led = Pin(16, Pin.OUT)

LOG_FILE = "farm_data_log.csv"
LOG_INTERVAL_S = 60

soil_dry = 52000
soil_wet = 22000

start_ms = time.ticks_ms()
last_log_ms = time.ticks_add(start_ms, -(LOG_INTERVAL_S * 1000))

def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value

def soil_percent():
    raw = soil.read_u16()
    span = soil_dry - soil_wet
    if span == 0:
        return 0
    percent = int(((soil_dry - raw) * 100) / span)
    return clamp(percent, 0, 100)

def climate_values():
    temp_c, humidity, pressure_hpa = read_bme280()
    return temp_c, humidity

def rain_state():
    return 1 if rain_sensor.value() == 0 else 0

def elapsed_seconds():
    return time.ticks_diff(time.ticks_ms(), start_ms) // 1000

def ensure_log_file():
    if LOG_FILE not in os.listdir():
        with open(LOG_FILE, "w") as handle:
            handle.write("elapsed_s,moisture,temp_c,humidity_pct,rain_detected\n")

def append_log(moisture, temp_c, humidity_pct, raining):
    with open(LOG_FILE, "a") as handle:
        handle.write("{},{},{},{},{}\n".format(elapsed_seconds(), moisture, temp_c, humidity_pct, raining))

def show_recent_logs(limit=3):
    with open(LOG_FILE, "r") as handle:
        lines = handle.readlines()
    for line in lines[-limit:]:
        print(line.strip())

ensure_log_file()
print("Smart farm data logger ready")

while True:
    try:
        moisture = soil_percent()
        temp_c, humidity_pct = climate_values()
        raining = rain_state()
    except Exception as error:
        print("Sensor error:", error)
        time.sleep(2)
        continue
    print("Soil:{}% Temp:{}C Hum:{}% Rain:{}".format(moisture, temp_c, humidity_pct, raining))
    if time.ticks_diff(time.ticks_ms(), last_log_ms) >= LOG_INTERVAL_S * 1000:
        append_log(moisture, temp_c, humidity_pct, raining)
        status_led.on()
        time.sleep(0.2)
        status_led.off()
        last_log_ms = time.ticks_ms()
        show_recent_logs()
    time.sleep(5)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|---|---|---|
| ensure_log_file() | Creates the CSV with a header row if it does not exist | Structured headers make later analysis much easier |
| elapsed_seconds() | Returns seconds since the Pico powered up | A data logger still works even without a real clock |
| append_log() | Adds one comma-separated row of sensor values | All important farm conditions end up in one reusable record |
| Status LED blink | Turns the LED on briefly after every successful write | Visual feedback helps detect logging problems early |

---

## Expected Result

The Pico should create a file named `farm_data_log.csv` and append new rows containing elapsed time, soil moisture, temperature, humidity, and rain state. The status LED should blink when each new row is written, and recent rows should appear in the Shell for quick verification.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---|---|---|
| No file is created | The log file path or file permissions may be wrong | Run the setup again and check `os.listdir()` in Thonny. |
| Rows contain strange values | One or more sensors were not calibrated or wired correctly | Test each sensor separately and update the calibration values. |
| LED never blinks | No logs are being written or the LED wiring is wrong | Check the log interval logic and the LED polarity. |
| Rain column is always the same | The rain sensor DOUT may not be responding to moisture | Test the rain input with a safe wet/dry demonstration. |

---

## Challenge Extensions

- Add a second log file that stores only daily summaries
- Send selected log values to a dashboard after each write in a future IoT upgrade
- Add light level as a fourth sensor to extend the farm record

---

## Reflection Questions

1. Why is a CSV log more useful than only watching live serial messages?
2. Why should a logger store several related farm variables together in one row?
3. What are the limits of using elapsed time instead of a real timestamp?
4. How would you choose a sensible logging interval for a real farm system?

---

## Save Your Work

Save the file to your computer as:

```
project_151_smart_farm_data_logger.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

Project 152: Soil Moisture Comparison System
