# Project 130
## Bluetooth Farm Monitoring Node

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

The real-world use case is a greenhouse corner, field demo, or remote area where local wireless monitoring is enough and internet access is not guaranteed.

Students will combine a soil sensor, a BME280 sensor, and BLE UART communication in one portable monitoring system.

The final system should advertise over BLE, stream live moisture and climate readings, and respond to simple commands from a BLE app.

### Project Story

This project creates a small farm-monitoring node that sends live environmental readings to a phone over BLE without needing Wi-Fi.

---

## Learning Objectives

- Set up BLE UART communication on the Pico 2 W
- Combine analog and digital sensor readings in one wireless report
- Use command-driven streaming instead of hard-wired serial-only output
- Avoid the common mistake of trying to use normal Bluetooth pairing for a BLE UART project
- Think about low-infrastructure monitoring for agriculture and environmental testing

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | BLE-capable controller | Use MicroPython |
| Soil moisture sensor | 1 | Analog moisture input | Calibrate for dry and wet soil |
| BME280 sensor module | 1 | Temperature, humidity, and pressure input | Requires bme280.py on the Pico |
| Phone with BLE app | 1 | Wireless monitor | Use nRF Connect, LightBlue, or similar BLE UART app |
| Breadboard and jumper wires | 1 | Prototype wiring | Keep the sensor wiring stable |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- These Bluetooth projects use the built-in `bluetooth` module plus two helper files: `ble_uart.py` and `ble_advertising.py`
- Save `ble_uart.py` to the Pico root folder as `ble_uart.py`
- Save `ble_advertising.py` to the Pico root folder as `ble_advertising.py`
- In Thonny Shell, run `import os; print(os.listdir())` and confirm both BLE helper files are visible on the Pico
- **Communication Setup**: install a BLE app such as nRF Connect, LightBlue, or another BLE UART terminal app on your phone
- Scan for the device name `AIDER_FarmNode` after the Pico starts advertising
- **Do not** pair from the normal phone Bluetooth settings menu. Open the BLE app, scan, connect to the UART-style service, then send text commands from inside the app
- If Bluetooth does not work, restart the Pico and rescan from the BLE app before changing the wiring
- Copy `bme280.py` to the Pico before running this project

### Project-Specific Safety Note

Do not force the phone to pair through normal Bluetooth settings for this BLE project.

Keep the soil sample away from the USB connector and Pico board.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Soil sensor AOUT | GPIO 26 | GPIO 26 / physical pin 31 | ADC input |
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
  │  GPIO 26 ───────────┤──── Soil Sensor AOUT
  │                     │
  │  GPIO 2  ───────────┤──── BME280 SDA
  │  GPIO 3  ───────────┤──── BME280 SCL
  │                     │
  │  3.3V    ───────────┤──── Soil Sensor VCC
  │  3.3V    ───────────┤──── BME280 VCC
  │  GND     ───────────┤──── Soil Sensor GND
  │  GND     ───────────┤──── BME280 GND
  │                     │
  └─────────────────────┘
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W
Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Position the Soil Moisture Sensor
Place the soil moisture probe so the sensing end can enter the soil sample. Identify VCC, GND, and AOUT / AO / Signal on the sensor module.

### Step 3: Connect the Soil Sensor
Connect soil sensor VCC to **3.3V**. Connect soil sensor GND to **GND**. Connect soil sensor AOUT, AO, or Signal to **GPIO 26** (ADC0).

### Step 4: Place the BME280 Sensor Module
Place the BME280 module where it can sense the air around the plant area. Identify VCC, GND, SDA, and SCL before wiring.

### Step 5: Connect the BME280 Sensor Module
Connect BME280 VCC to **3.3V**. Connect BME280 GND to **GND**. Connect BME280 SDA to **GPIO 2** and BME280 SCL to **GPIO 3**.

### Step 6: Load the BLE Helper Files
Upload `ble_uart.py` and `ble_advertising.py` to the Pico root folder before running the main code. In the Thonny Shell, use `os.listdir()` to confirm the helper files are on the Pico.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Soil sensor VCC connects to 3.3V
- [x] Soil sensor GND connects to GND
- [x] Soil sensor AOUT / AO / Signal connects to GPIO 26
- [x] BME280 VCC connects to 3.3V
- [x] BME280 GND connects to GND
- [x] BME280 SDA connects to GPIO 2
- [x] BME280 SCL connects to GPIO 3
- [x] BLE helper files are saved on the Pico
- [x] No loose jumper wires

> **Intermediate Note**
> This project uses BLE on the Raspberry Pi Pico 2W. Use a BLE app such as nRF Connect, LightBlue, or a BLE UART terminal to connect to `AIDER_FarmNode`. Test dry and wet soil readings before streaming data. The BME280 needs a short delay between readings.

> **Safety Note**
> Do not pour water onto the Pico, breadboard, USB cable, or jumper wires. Add water to the soil sample away from the electronics.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the two sensor paths first and confirm their wiring labels
- Do not start BLE debugging until the sensors can be read locally

### Test the Input Sensors

- Run a quick ADC test for the soil sensor and a short BME280 test for the climate sensor
- Capture dry and wet reference values for the moisture sensor

### Test Communication

- Upload the final code and scan for `AIDER_FarmNode` in the BLE app
- Connect to the BLE UART-style service and watch the streamed readings appear
- Send `status`, `stream off`, and `stream on` to confirm the command interface works

### Run the Full System

- Let the node stream data for several cycles and compare the values with real environmental changes
- Move the soil sensor between drier and wetter samples and observe the wireless updates

### Save the Project

- Save the working code and record the BLE device name and report interval
- Write down which commands were supported by your final version

### Additional Testing and Calibration Checks

**Calibration and tuning notes**

- Use a BLE app, not the phone's normal Bluetooth settings page
- Test the sensors locally before assuming a BLE problem
- If the BLE connection is unstable, restart the Pico and rescan from the BLE app
- If the BME280 occasionally fails, keep the report interval long enough for reliable reads

**Quick testing checklist**

- [ ] `AIDER_FarmNode` appears in the BLE app scan list
- [ ] The app connects to the BLE UART-style service successfully
- [ ] Live data streams to the phone
- [ ] `status` returns a fresh reading on demand
- [ ] `stream off` and `stream on` change the reporting behaviour

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, I2C, Pin
import bluetooth
import bme280
import time
from ble_uart import BLEUART

DEVICE_NAME = "AIDER_FarmNode"
REPORT_INTERVAL_S = 5

soil = ADC(26)

i2c_bme = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
bme = bme280.BME280(i2c=i2c_bme)


def number_from_bme(text_value):
    cleaned = "".join(ch for ch in str(text_value) if ch.isdigit() or ch in ".-")
    return float(cleaned)


def read_bme280():
    temp_text, pressure_text, humidity_text = bme.values
    return number_from_bme(temp_text), number_from_bme(humidity_text), number_from_bme(pressure_text)


dry_reading = 52000
wet_reading = 22000

ble = bluetooth.BLE()
ble.active(True)
uart = BLEUART(ble, name=DEVICE_NAME)

stream_enabled = True
last_report = 0
command_queue = []


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def soil_percent():
    raw = soil.read_u16()
    span = dry_reading - wet_reading
    if span == 0:
        return 0
    percent = int(((dry_reading - raw) * 100) / span)
    return clamp(percent, 0, 100)


def environment_values():
    temp_c, humidity, pressure_hpa = read_bme280()
    return temp_c, humidity


def send_line(message):
    print(message)
    uart.write((message + "\n").encode())


def on_rx(data):
    command = data.decode("utf-8").strip().lower()
    if command:
        command_queue.append(command)


uart.on_rx(on_rx)
send_line("Bluetooth farm node ready")

while True:
    now = time.time()

    if stream_enabled and (now - last_report) >= REPORT_INTERVAL_S:
        try:
            moisture = soil_percent()
            temp_c, humidity_pct = environment_values()
            send_line("Moisture:{}% Temp:{}C Hum:{}%".format(moisture, temp_c, humidity_pct))
        except Exception as error:
            send_line("Sensor error: {}".format(error))
        last_report = now

    if command_queue:
        command = command_queue.pop(0)
        if command == "status":
            try:
                moisture = soil_percent()
                temp_c, humidity_pct = environment_values()
                send_line("Status Moisture:{}% Temp:{}C Hum:{}%".format(moisture, temp_c, humidity_pct))
            except Exception as error:
                send_line("Status failed: {}".format(error))
        elif command == "stream on":
            stream_enabled = True
            send_line("Streaming enabled")
        elif command == "stream off":
            stream_enabled = False
            send_line("Streaming disabled")
        elif command == "help":
            send_line("Commands: status, stream on, stream off, help")
        else:
            send_line("Unknown command")

    time.sleep(0.2)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| BLEUART setup | Initialises the Bluetooth UART service | This is the wireless link between the Pico and the phone |
| `command_queue` and `on_rx()` | Queues incoming BLE commands for processing | Command parsing is easier when messages are queued |
| `stream_enabled` and `REPORT_INTERVAL_S` | Control periodic data transmission | Students can turn streaming on and off without rewiring |
| `status` command | Returns an immediate sensor reading | On-demand reporting is useful when continuous streaming is disabled |

---

## Expected Result

After the Pico starts, a BLE app should find the device name `AIDER_FarmNode`. Once connected, the phone should receive live moisture, temperature, and humidity updates. Sending the supported commands should change the streaming behaviour or request an instant status message.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The phone cannot find the device | BLE helper files are missing or the Pico is not advertising | Confirm `ble_uart.py` and `ble_advertising.py` are on the Pico, then restart the board |
| The phone tries to pair but nothing works | Using normal Bluetooth settings instead of a BLE app | Open a BLE app and connect to the BLE UART service instead of pairing in settings |
| Streaming works but the values are wrong | Sensor calibration or wiring is incorrect | Record fresh calibration values and test the BME280 sensor wiring separately |
| Commands are ignored | The command text does not match the expected format | Send the exact commands shown in the help message |

---

## Challenge Extensions

- Add a battery-voltage estimate so the node can report its own power state
- Add a Bluetooth command to capture dry and wet moisture references wirelessly
- Add a local OLED so the node can be read even without a phone connection

---

## Reflection Questions

1. Why might BLE be a better choice than Wi-Fi for some short-range farm-monitoring tasks?
2. Why is it important to explain the difference between BLE apps and normal Bluetooth pairing?
3. What are the trade-offs between streaming continuously and sending only status on demand?
4. How would you mount this node so the wireless link and the sensor wiring both remain reliable?

---

## Save Your Work

Save the file to your computer as:

```
project_130_bluetooth_farm_monitoring_node.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 131: Smart Water Tank Refill System**