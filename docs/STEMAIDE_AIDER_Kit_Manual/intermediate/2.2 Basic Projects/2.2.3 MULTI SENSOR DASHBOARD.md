# Project 113
## MULTI SENSOR DASHBOARD

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

This project combines a BME280 climate sensor and a soil moisture sensor into one BLE dashboard node.

The Pico collects multiple inputs, calculates a simple plant-condition summary, and sends the combined report to a phone.

The final system should stream or report temperature, humidity, pressure, soil moisture, and a simple plant condition such as NORMAL or HOT AND DRY.

### Project Story

The real-world use case is a small plant station or greenhouse corner where students need several readings in one place instead of separate tools.

---

## Learning Objectives

- Integrate multiple sensors into one system
- Calibrate soil moisture while also reading I2C environmental data
- Build a simple dashboard-style text report
- Use rule-based decision logic to summarise overall plant condition
- Test each sensor path before combining the full system

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller with BLE support | Use MicroPython |
| BME280 sensor module | 1 | Temperature, humidity, and pressure input | Use a 3.3V-compatible breakout |
| Soil moisture sensor | 1 | Analog soil input | A capacitive sensor is preferred |
| Breadboard and jumper wires | 1 set | Connections | Keep I2C and ADC wiring tidy |
| Phone with BLE app | 1 | Wireless dashboard viewer | Use a BLE UART-style app |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- Software Installation and Setup
- Safety Guidelines
- Breadboard Basics
- Reading Circuit Diagrams

### Project-Specific Setup Notes

- These Bluetooth projects use the built-in `bluetooth` module plus two helper files: `ble_uart.py` and `ble_advertising.py`
- Save `ble_uart.py` to the Pico root folder as `ble_uart.py`
- Save `ble_advertising.py` to the Pico root folder as `ble_advertising.py`
- Save `BME280.py` to the Pico root folder as `BME280.py`
- In Thonny Shell, run `import os; print(os.listdir())` and confirm all project library files are visible on the Pico
- Communication Setup: install a BLE app such as nRF Connect, LightBlue, or another BLE UART terminal app on your phone
- Scan for the device name `AIDER_Dashboard` after the Pico starts advertising
- **Do not** pair from the normal phone Bluetooth settings menu. Open the BLE app, scan, connect to the UART-style service, then send text commands from inside the app
- If Bluetooth does not work, restart the Pico and rescan from the BLE app before changing the wiring

### Project-Specific Safety Note

Keep electronics away from water and dry your hands before touching the circuit. Place sensors in water only after the Pico is stable and the wiring has been checked. Do not let exposed jumper connections touch water. Do not let the soil sensor or wet sample touch the Pico or the BME280 wiring.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| BME280 VCC | 3.3V | Physical pin 36 | Sensor power |
| BME280 GND | GND | Physical pin 38 | Common ground |
| BME280 SDA | GPIO 8 | GPIO 8 / physical pin 11 | I2C0 SDA |
| BME280 SCL | GPIO 9 | GPIO 9 / physical pin 12 | I2C0 SCL |
| Soil sensor VCC | 3.3V | Physical pin 36 | Sensor power |
| Soil sensor GND | GND | Physical pin 38 | Common ground |
| Soil sensor AOUT | GPIO 26 | GPIO 26 / physical pin 31 | ADC0 input |

---

## Wiring Diagram

![Circuit Diagram](../../assets/intermidiate/MULTI SENSOR DASHDOARD/circuit_1.png)

```text
Raspberry Pi Pico 2 W
┌─────────────────────┐
│                     │
│  GPIO 8  ───────────┤──── BME280 SDA
│  GPIO 9  ───────────┤──── BME280 SCL
│  3.3V  ─────────────┤──── BME280 VCC and soil sensor VCC
│  GND   ─────────────┤──── BME280 GND and soil sensor GND
│  GPIO 26 ───────────┤──── Soil sensor AOUT (ADC0)
│                     │
└─────────────────────┘
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W

Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Place the BME280 Sensor

Place the BME280 module on the breadboard or hold it beside the breadboard with jumper wires. Check the printed labels and identify VCC, GND, SDA, and SCL.

### Step 3: Connect BME280 VCC

Connect BME280 VCC to 3.3V.

### Step 4: Connect BME280 GND

Connect BME280 GND to GND.

### Step 5: Connect BME280 SDA

Connect BME280 SDA to GPIO 8.

### Step 6: Connect BME280 SCL

Connect BME280 SCL to GPIO 9.

### Step 7: Position the Soil Moisture Sensor

Place the soil moisture probe so the sensing end can enter the soil sample. Identify VCC, GND, and AOUT / AO / Signal on the soil sensor module.

### Step 8: Connect Soil Sensor VCC

Connect the soil sensor VCC pin to 3.3V.

### Step 9: Connect Soil Sensor GND

Connect the soil sensor GND pin to GND.

### Step 10: Connect Soil Sensor AOUT

Connect the soil sensor AOUT, AO, or Signal pin to GPIO 26 (ADC0).

### Step 11: Separate the Wet Sample

Keep wet soil and the soil sensor probe away from the BME280, Pico, breadboard, USB cable, and jumper wires.

---

## Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] BME280 VCC connects to 3.3V
- [x] BME280 GND connects to GND
- [x] BME280 SDA connects to GPIO 8
- [x] BME280 SCL connects to GPIO 9
- [x] Soil sensor VCC connects to 3.3V
- [x] Soil sensor GND connects to GND
- [x] Soil sensor AOUT / AO / Signal connects to GPIO 26
- [x] No loose jumper wires

> **Intermediate Note**
>
> This project uses BLE on the Raspberry Pi Pico 2W. Use a BLE app such as nRF Connect, LightBlue, or a BLE UART terminal to connect to `AIDER_Dashboard` and send commands. If the BME280 does not respond, run an I2C scanner before the full dashboard code. Test dry and wet soil before trusting moisture thresholds.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware setup

- Build the BME280 wiring first, then add the soil sensor
- Keep the system layout organised because two sensor types are being used

### Test the input sensors

- Run `i2c.scan()` and a short BME280 test script
- Run a short ADC test for the soil sensor and record dry and wet readings

### Test the output data

- Upload the final code and check the dashboard lines in the Shell first
- Confirm that both climate data and soil data appear in the report

### Test communication

- Connect to `AIDER_Dashboard` from the BLE app
- Send `status`, `read`, `dry`, `wet`, `stream on`, and `stream off` to verify the interface

### Run the full system

- Capture the soil dry and wet references
- Enable streaming and observe the combined dashboard output
- Check that the plant condition changes if the soil is dry or if the temperature becomes too high

### Save the project

- Save the final code and note the calibration values used for the soil sensor
- Compare this combined dashboard with the single-sensor projects you completed earlier

---

## Full Project Code

```python
from machine import ADC, I2C, Pin
import bluetooth
import time
import BME280
from ble_uart import BLEUART

DEVICE_NAME = "AIDER_Dashboard"
REPORT_INTERVAL_MS = 3000

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=100000)
bme = BME280.BME280(i2c=i2c)
soil = ADC(26)

ble = bluetooth.BLE()
ble.active(True)
uart = BLEUART(ble, name=DEVICE_NAME)

dry_reading = 52000
wet_reading = 22000
stream_enabled = True
last_report_ms = time.ticks_ms()
command_queue = []


def send_line(message):
    print(message)
    uart.write((message + "\n").encode())


def on_rx(data):
    command = data.decode("utf-8").strip().lower()
    if command:
        command_queue.append(command)


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def first_number(text):
    digits = ""
    for char in text:
        if char in "-0123456789.":
            digits += char
        elif digits:
            break
    return float(digits)


def soil_percent(raw_value):
    span = dry_reading - wet_reading
    if span == 0:
        return 0
    percent = int(((dry_reading - raw_value) * 100) / span)
    return clamp(percent, 0, 100)


def plant_state(soil_pct, temp_c, humidity_pct):
    if soil_pct < 35 and temp_c > 30:
        return "HOT AND DRY"
    if soil_pct < 35:
        return "DRY"
    if humidity_pct < 35:
        return "AIR DRY"
    return "NORMAL"


def current_report():
    raw_soil = soil.read_u16()
    soil_pct = soil_percent(raw_soil)
    temp_text = bme.temperature
    humidity_text = bme.humidity
    pressure_text = bme.pressure
    temp_c = first_number(temp_text)
    humidity_pct = first_number(humidity_text)
    state = plant_state(soil_pct, temp_c, humidity_pct)
    return raw_soil, soil_pct, temp_text, humidity_text, pressure_text, state


def send_dashboard():
    raw_soil, soil_pct, temp_text, humidity_text, pressure_text, state = current_report()
    send_line("Temp:{} Hum:{} Press:{}".format(temp_text, humidity_text, pressure_text))
    send_line("Soil:{}% Raw:{} State:{}".format(soil_pct, raw_soil, state))


uart.on_rx(on_rx)
send_line("Bluetooth multi-sensor dashboard ready")

while True:
    now = time.ticks_ms()
    if stream_enabled and time.ticks_diff(now, last_report_ms) >= REPORT_INTERVAL_MS:
        send_dashboard()
        last_report_ms = now

    if command_queue:
        command = command_queue.pop(0)
        if command in ("status", "read"):
            send_dashboard()
        elif command == "stream on":
            stream_enabled = True
            send_line("Streaming enabled")
        elif command == "stream off":
            stream_enabled = False
            send_line("Streaming disabled")
        elif command == "dry":
            dry_reading = soil.read_u16()
            send_line("Dry reference captured: {}".format(dry_reading))
        elif command == "wet":
            wet_reading = soil.read_u16()
            send_line("Wet reference captured: {}".format(wet_reading))
        elif command == "help":
            send_line("Commands: status, read, stream on, stream off, dry, wet, help")
        else:
            send_line("Unknown command. Send help.")

    time.sleep_ms(200)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| Two sensor paths | Read climate data from the BME280 and moisture data from the ADC sensor | A dashboard needs data from multiple inputs |
| Soil calibration | Uses dry and wet reference values to scale the soil reading | Makes the dashboard moisture value more useful |
| `plant_state()` | Summarises several readings into one condition label | Students see how system logic combines multiple inputs |
| `send_dashboard()` | Formats the report into clear text lines | Keeps the BLE output consistent and easy to read |

---

## Expected Result

The BLE app receives a compact dashboard report that includes climate data, soil moisture, and a simple plant-condition summary. The report updates when streaming is enabled or when the user requests a status reading.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| Only one sensor appears to work | The I2C sensor or the ADC sensor path has a wiring issue | Test the BME280 and soil sensor separately, then reconnect them to the combined system. |
| Soil percentage looks unrealistic | The dry and wet references were not calibrated | Capture dry and wet values again before trusting the dashboard output. |
| State summary is misleading | The decision rules do not match your test environment | Adjust the threshold logic after observing several real readings. |
| Phone cannot find the BLE device | The Pico is not advertising or the BLE helper files are missing | Confirm `ble_uart.py` and `ble_advertising.py` are saved on the Pico, restart the board, and scan again from nRF Connect or LightBlue. |
| Commands do not change the system state | The phone is connected to the wrong service or the command text is different from the expected command | Reconnect to the BLE UART service and send the exact command shown in the test section. |

---

## Challenge Extensions

- Add an OLED display so the same dashboard appears locally and over BLE
- Send comma-separated dashboard data so it can be copied into a spreadsheet or graphing tool
- Add a relay or buzzer output that reacts only when the combined condition becomes critical

---

## Reflection Questions

1. Why is a combined dashboard more useful than reading each sensor in a separate project?
2. How does a poor calibration on one sensor affect the trustworthiness of the whole dashboard?
3. If you were designing a real greenhouse monitor, what extra sensor would you add next?

---

## Save Your Work

Save the file to your computer as:

```
project_113_multi_sensor_dashboard.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

Project 114: Smart Timer
