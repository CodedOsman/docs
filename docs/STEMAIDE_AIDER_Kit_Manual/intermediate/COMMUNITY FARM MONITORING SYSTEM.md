# Project 179
## COMMUNITY FARM MONITORING SYSTEM

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

The real-world use case is a school or community farm where one zone may dry faster than another and the team needs to decide which area needs attention first.

Students will combine two soil moisture sensors, a BME280 climate sensor, and priority logic that identifies the zone needing the most urgent response.

The final system should print both zone readings, classify each zone, highlight the priority zone, and drive simple LEDs that show whether the overall farm condition needs attention.

### Project Story

This project builds a two-zone monitoring system that helps students compare conditions across different planting areas in the same farm setup.

---

## Learning Objectives

- Read and compare data from more than one growing zone
- Use two ADC inputs on the Pico for multi-zone monitoring
- Build priority logic that identifies the most urgent zone first
- Combine zone data with a shared climate reading
- Explain why one average reading can hide a local problem
- Use simple indicators to summarise a larger monitoring problem

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board | Use MicroPython firmware |
| Soil moisture sensor (analog output) | 1 | Measure Zone A and Zone B separately | Keep both sensor electronics sections dry |
| BME280 sensor module | 1 | Temperature, humidity, and pressure input | Requires bme280.py on the Pico |
| Green LED and 220 Ω resistor | 1 each | Shows all zones are currently acceptable | Use current limiting |
| Red LED and 220 Ω resistor | 1 each | Shows one or more zones need attention | Use current limiting |
| Breadboard and jumper wires | 1 | Prototype wiring | Disconnect power before rewiring |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules
- Run `import os` and `print(os.listdir())` in the Thonny Shell to confirm the Pico file system is responding before you save the code
- If you are using a bare BME280 sensor instead of a ready-made module, add a 10 kΩ I2C pull-up resistors already included on most BME280 modules

### Project-Specific Safety Note

Keep electronics away from water and wet surfaces.

Label the two soil probes clearly so Zone A and Zone B do not get mixed up during testing.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Zone A soil sensor VCC | Physical pin 36 | Physical pin 36 | Sensor power |
| Zone A soil sensor GND | Any GND pin | Any GND pin | Common ground |
| Zone A soil sensor AOUT | GPIO 26 / physical pin 31 | GPIO 26 / physical pin 31 | Analog zone A input |
| Zone B soil sensor VCC | Physical pin 36 | Physical pin 36 | Sensor power |
| Zone B soil sensor GND | Any GND pin | Any GND pin | Common ground |
| Zone B soil sensor AOUT | GPIO 27 / physical pin 32 | GPIO 27 / physical pin 32 | Analog zone B input |
| Green LED anode | GPIO 16 through 220 Ω resistor | GPIO 16 / physical pin 21 | All-zones-OK indicator |
| Red LED anode | GPIO 17 through 220 Ω resistor | GPIO 17 / physical pin 22 | Attention-needed indicator |
| LED cathodes | GND | Any GND pin | Return path |
| BME280 VCC | 3.3V | Physical pin 36 | Sensor power |
| BME280 GND | GND | Any GND pin | Common ground |
| BME280 SDA | GPIO 2 | GPIO 2 / physical pin 4 | I2C data |
| BME280 SCL | GPIO 3 | GPIO 3 / physical pin 5 | I2C clock |

---

## Wiring Diagram

```
  Zone A soil sensor AOUT -> GPIO 26
  Zone B soil sensor AOUT -> GPIO 27
  BME280 SDA              -> GPIO 2
  BME280 SCL              -> GPIO 3
  BME280 VCC              -> 3.3V
  BME280 GND              -> GND
  GPIO 16 -> 220Ω -> Green LED anode
  GPIO 17 -> 220Ω -> Red LED anode
  LED cathodes            -> GND
  All sensors             -> 3.3V and GND
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W
Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Label the Two Soil Zones
Label the two soil moisture probes as Zone A and Zone B before wiring. Identify VCC, GND, and AOUT / AO / Signal on each soil sensor.

### Step 3: Connect Zone A Soil Sensor
Connect Zone A soil sensor VCC to 3.3V. Connect Zone A soil sensor GND to GND. Connect Zone A AOUT, AO, or Signal to GPIO 26.

### Step 4: Connect Zone B Soil Sensor
Connect Zone B soil sensor VCC to 3.3V. Connect Zone B soil sensor GND to GND. Connect Zone B AOUT, AO, or Signal to GPIO 27.

### Step 5: Place the BME280 Sensor Module
Place the BME280 module where it can sense the shared farm area. Connect BME280 VCC to 3.3V. Connect BME280 GND to GND. Connect BME280 SDA to GPIO 2 and BME280 SCL to GPIO 3. If your BME280 is bare, use the module pins labeled VCC, GND, SDA, and SCL.

### Step 6: Place and Connect the Indicator LEDs
Place the green OK LED and red alert LED on the breadboard. Connect the green LED long leg through a 220Ω resistor to GPIO 16. Connect the red LED long leg through a 220Ω resistor to GPIO 17. Connect both LED short legs to GND.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Zone A soil signal connects to GPIO 26
- [x] Zone B soil signal connects to GPIO 27
- [x] BME280 SDA connects to GPIO 2 and SCL connects to GPIO 3
- [x] Green LED long leg connects through a 220Ω resistor to GPIO 16
- [x] Red LED long leg connects through a 220Ω resistor to GPIO 17
- [x] Both LED short legs connect to GND
- [x] Zone labels are attached to the correct probes
- [x] No loose jumper wires

> **Intermediate Note**
> Calibrate each soil zone separately and label the probes physically so the community farm data does not mix up Zone A and Zone B. The BME280 needs a short delay between readings.

> **Safety Note**
> Do not pour water onto the Pico, breadboard, USB cable, or jumper wires. Add water to soil samples away from the electronics.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the two soil-sensor channels carefully so the signals do not get mixed up
- Add the BME280 and LEDs only after the zone wiring is clearly labelled

### Test the Input Sensor

- Record dry and wet readings for both soil sensors and confirm that each ADC channel responds independently
- Read the BME280 locally and confirm the climate values are stable

### Test the Output Device

- Force an attention condition in one zone and confirm the red LED turns on while the green LED turns off
- Return both zones to acceptable conditions and confirm the green LED comes back on

### Test Communication

- Watch the serial output and confirm it prints both zone values, each zone state, the average, and the priority zone
- Use the serial information to explain why one zone was selected first

### Run the Full System

- Create different moisture conditions in Zone A and Zone B and confirm the system identifies the drier zone correctly
- Compare the zone values with the shared climate reading to discuss how one climate can still hide local soil differences

### Save the Project

- Save the final code and record the zone thresholds and observations from your comparison tests
- Write down what kinds of decisions a community farm team could make from the priority-zone output

### Additional Testing and Calibration Checks

- **Dry/wet reading test**: calibrate both soil sensors and confirm each one responds on the correct ADC channel
- **Normal condition test**: keep both zones moist and confirm the system reports OK with the green LED on
- **Threshold condition test**: dry one zone more than the other and confirm the priority message identifies the right zone
- **Output response test**: confirm the LEDs change according to the combined zone states
- **Calibration note**: if one sensor reads consistently higher or lower than the other, document that offset and retest
- **BME280 test**: confirm the climate reading is stable while you compare the soil zones

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, I2C, Pin
import bme280
import time

zone_a_sensor = ADC(26)
zone_b_sensor = ADC(27)
i2c_bme = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
bme = bme280.BME280(i2c=i2c_bme)


def number_from_bme(text_value):
    cleaned = "".join(ch for ch in str(text_value) if ch.isdigit() or ch in ".-")
    return float(cleaned)


def read_bme280():
    temp_text, pressure_text, humidity_text = bme.values
    return number_from_bme(temp_text), number_from_bme(humidity_text), number_from_bme(pressure_text)


ok_led = Pin(16, Pin.OUT)
alert_led = Pin(17, Pin.OUT)

SOIL_DRY = 52000
SOIL_WET = 22000
DRY_THRESHOLD = 35
WATCH_THRESHOLD = 45
WINDOW_SIZE = 8

zone_a_history = []
zone_b_history = []


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def average(values):
    if not values:
        return 0
    return sum(values) / len(values)


def soil_percent(sensor):
    raw = sensor.read_u16()
    span = SOIL_DRY - SOIL_WET
    if span <= 0:
        return 0
    percent = int(((SOIL_DRY - raw) * 100) / span)
    return clamp(percent, 0, 100)


def update_history(history, value):
    history.append(value)
    if len(history) > WINDOW_SIZE:
        history.pop(0)


def zone_state(moisture):
    if moisture <= DRY_THRESHOLD:
        return 'DRY'
    if moisture <= WATCH_THRESHOLD:
        return 'WATCH'
    return 'OK'


def priority_zone(zone_a, zone_b):
    if zone_a <= DRY_THRESHOLD and zone_b <= DRY_THRESHOLD:
        return 'BOTH ZONES NEED ATTENTION'
    if zone_a < zone_b:
        return 'ZONE A'
    if zone_b < zone_a:
        return 'ZONE B'
    return 'EQUAL PRIORITY'


def read_climate():
    try:
        temp_c, humidity, pressure_hpa = read_bme280()
        return temp_c, humidity
    except Exception as error:
        print('BME28022 read error:', error)
        return None, None


print('=== Community Farm Monitoring System ===')
print('Comparing Zone A and Zone B conditions.\n')

while True:
    zone_a = soil_percent(zone_a_sensor)
    zone_b = soil_percent(zone_b_sensor)
    temp_c, humidity = read_climate()

    update_history(zone_a_history, zone_a)
    update_history(zone_b_history, zone_b)

    state_a = zone_state(zone_a)
    state_b = zone_state(zone_b)
    priority = priority_zone(zone_a, zone_b)

    if state_a == 'OK' and state_b == 'OK':
        ok_led.value(1)
        alert_led.value(0)
    else:
        ok_led.value(0)
        alert_led.value(1)

    print('Zone A: {}% ({}) | Zone B: {}% ({}) | Avg A: {:.1f}% | Avg B: {:.1f}% | Temp: {} | Humidity: {} | Priority: {}'.format(
        zone_a,
        state_a,
        zone_b,
        state_b,
        average(zone_a_history),
        average(zone_b_history),
        temp_c,
        humidity,
        priority
    ))
    time.sleep(5)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| Two ADC channels | Reads separate soil sensors on GPIO 26 and GPIO 27 | This is the key change from a single-zone monitor |
| zone_state() | Classifies each zone as DRY, WATCH, or OK | Students can compare local conditions instead of only seeing raw values |
| priority_zone() | Compares both zones and identifies which needs attention first | This turns multi-zone data into a practical action decision |
| History averages | Maintains a rolling average for each zone | An average can help show whether one zone is consistently drier than another |

---

## Expected Result

The serial monitor should print separate readings for Zone A and Zone B along with a shared temperature and humidity reading.

When one zone becomes drier than the other, the priority-zone message should identify that zone first.

If either zone is in WATCH or DRY state, the red LED should turn on and the green LED should turn off.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| Zone A and Zone B always read the same | Wiring mix-up or swapped probes | Recheck GPIO 26 and GPIO 27 and label the two probes clearly |
| The wrong zone gets priority | Probes are swapped relative to labels | Swap the probes back or update the labels and retest with one dry sample at a time |
| The LEDs never show OK | One zone is always below the watch threshold or a sensor is poorly calibrated | Check both soil values and review the threshold settings |
| BME280 readings are missing | Wiring or I2C address issue | Check BME280 VCC, GND, SDA, and SCL connections |

---

## Challenge Extensions

- Decide how you would extend this two-zone system to four zones without making the user interface confusing
- Design a fair rule for choosing the priority zone when one area is slightly drier but another area contains more sensitive plants
- Add Wi-Fi reporting so the multi-zone summary can be viewed from a phone
- Add a buzzer that sounds only when both zones are dry at the same time
- Add an OLED page that cycles through Zone A, Zone B, and the overall priority summary
- Add a third soil sensor if extra ADC hardware is available in your expanded design

---

## Reflection Questions

1. Why can one average farm reading hide a serious local problem?
2. Why is it useful to classify each zone separately before making an overall decision?
3. How would you explain a priority-zone decision to a volunteer team on a community farm?
4. What extra information would help you decide which zone to water first?

---

## Save Your Work

Save the file to your computer as:

```
project_179_community_farm_monitoring_system.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 180: Smart Irrigation Optimization Demo**