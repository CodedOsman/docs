# Project 132
## IOT FARM DASHBOARD

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

The real-world use case is a greenhouse bench, crop tray, or plant station where students need one simple page that summarises several readings at once.

Students will combine soil moisture, temperature, humidity, and a rule-based plant-state summary into one Wi-Fi dashboard.

The final system should display an auto-refreshing page that shows the current readings and a simple condition such as NORMAL, DRY, or HOT AND DRY.

### Project Story

This project creates a small farm dashboard that serves live sensor data over Wi-Fi to a browser on the same network.

---

## Learning Objectives

- Serve a browser dashboard from the Pico 2 W
- Combine multiple readings into one web-friendly status page
- Use simple rule-based logic to summarise plant condition
- Test a multi-sensor IoT page from a phone or laptop on the same network
- Understand how dashboard design can simplify system monitoring

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Wi-Fi capable controller | Use MicroPython |
| Soil moisture sensor | 1 | Analog moisture input | Calibrate before final use |
| BME280 sensor module | 1 | Temperature, humidity, and pressure input | Requires bme280.py on the Pico |
| Phone or computer | 1 | Dashboard viewer | Must be on the same Wi-Fi network |
| Breadboard and jumper wires | 1 | Prototype wiring | Keep analog wiring neat |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules
- **Communication Setup**: connect the Pico 2 W and your phone or computer to the same Wi-Fi network
- Replace the SSID and PASSWORD placeholders in the code before testing the network features
- After upload, read the IP address shown in the Thonny Shell and use that address in a browser if the project serves a page
- No external library is required. This project uses the built-in `network`, `socket`, and `dht` modules

### Project-Specific Safety Note

Do not expose real Wi-Fi passwords in screenshots of the dashboard or Thonny Shell.

Keep the soil sample and sensor moisture away from the USB connection and Pico board.

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
Place the soil moisture probe so the sensing end can enter the soil sample. Identify VCC, GND, and AOUT / AO / Signal before wiring.

### Step 3: Connect the Soil Sensor
Connect soil sensor VCC to **3.3V**. Connect soil sensor GND to **GND**. Connect soil sensor AOUT, AO, or Signal to **GPIO 26** (ADC0).

### Step 4: Place the BME280 Sensor Module
Place the BME280 module where it can sense the air around the farm demo area. Identify VCC, GND, SDA, and SCL before wiring.

### Step 5: Connect the BME280 Sensor Module
Connect BME280 VCC to **3.3V**. Connect BME280 GND to **GND**. Connect BME280 SDA to **GPIO 2** and BME280 SCL to **GPIO 3**.

### Step 6: Prepare for Dashboard Testing
Keep the hardware wiring complete before opening the dashboard page. Your phone or computer must be on the same Wi-Fi network as the Pico 2W.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Soil sensor VCC connects to 3.3V
- [x] Soil sensor GND connects to GND
- [x] Soil sensor AOUT / AO / Signal connects to GPIO 26
- [x] BME280 VCC connects to 3.3V
- [x] BME280 GND connects to GND
- [x] BME280 SDA connects to GPIO 2 and SCL connects to GPIO 3
- [x] Pico 2W and browser device are on the same Wi-Fi network for the dashboard
- [x] No loose jumper wires

> **Intermediate Note**
> When running the networking part, the Pico 2W must be connected to Wi-Fi. Replace the SSID and PASSWORD placeholders in the MicroPython code before testing. Open the IP address shown in the Thonny Shell from a browser on the same local network. The BME280 needs a short delay between readings.

> **Safety Note**
> Do not pour water onto the Pico, breadboard, USB cable, or jumper wires. Keep the soil sample and sensor moisture away from the USB connection.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the two sensor circuits first and keep the wiring labelled
- Do not begin network testing until the sensor values can be read locally

### Test the Input Sensors

- Check the soil sensor and record dry and wet references
- Run a short BME280 script and confirm that temperature and humidity values appear

### Test Communication

- Connect the Pico to Wi-Fi and note the IP address printed in Thonny
- Open the page in a browser on the same Wi-Fi network and confirm that the dashboard loads

### Run the Full System

- Observe the auto-refreshing page and compare the displayed values with real changes in the environment
- Change one condition at a time, such as drying the soil or covering the sensor, to watch the plant-state summary change

### Save the Project

- Save the final code and note the IP address behaviour on your test network
- Record the thresholds used in `plant_state()` so later projects can reuse them

### Additional Testing and Calibration Checks

**Calibration and tuning notes**

- Calibrate the soil sensor before trusting the dashboard summary
- Use the same Wi-Fi network for the Pico and the viewing device
- If the page loads slowly, refresh less often or simplify the network environment during testing
- Change only one condition at a time so you can tell which rule changed the state

**Quick testing checklist**

- [ ] Wi-Fi connection succeeds and an IP address appears
- [ ] The dashboard page loads in a browser
- [ ] Soil, temperature, and humidity values appear correctly
- [ ] The page refreshes automatically
- [ ] The plant-state summary changes when conditions change

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
import network
import socket
import time
from machine import ADC, I2C, Pin
import bme280

SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

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


def climate_values():
    temp_c, humidity, pressure_hpa = read_bme280()
    return temp_c, humidity


def plant_state(moisture, temp_c, humidity_pct):
    if moisture < 35 and temp_c > 30:
        return "HOT AND DRY"
    if moisture < 35:
        return "DRY"
    if humidity_pct > 80:
        return "TOO HUMID"
    return "NORMAL"


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        start = time.time()
        while not wlan.isconnected():
            if time.time() - start > 20:
                raise RuntimeError("Wi-Fi connection timeout")
            time.sleep(0.5)
    print("Wi-Fi connected:", wlan.ifconfig()[0])
    return wlan


def dashboard_page(ip_address, moisture, temp_c, humidity_pct, state):
    return """HTTP/1.1 200 OK
Content-Type: text/html
Connection: close

<!DOCTYPE html>
<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
<meta http-equiv='refresh' content='5'>
<title>IoT Farm Dashboard</title>
<style>body{font-family:Arial;margin:20px;} .card{padding:12px;border:1px solid #ccc;border-radius:8px;margin-bottom:12px;}</style>
</head><body>
<h2>IoT Farm Dashboard</h2>
<div class='card'>IP: {ip}</div>
<div class='card'>Soil Moisture: {moisture}%</div>
<div class='card'>Temperature: {temp}C</div>
<div class='card'>Humidity: {humidity}%</div>
<div class='card'>Plant State: {state}</div>
</body></html>""".format(
        ip=ip_address,
        moisture=moisture,
        temp=temp_c,
        humidity=humidity_pct,
        state=state,
    )


wlan = connect_wifi()
ip_address = wlan.ifconfig()[0]

server = socket.socket()
server.bind(("0.0.0.0", 80))
server.listen(1)

print("Open http://{}".format(ip_address))

while True:
    moisture = soil_percent()
    try:
        temp_c, humidity_pct = climate_values()
    except Exception:
        temp_c, humidity_pct = 0, 0

    state = plant_state(moisture, temp_c, humidity_pct)

    print("Soil:{}% Temp:{}C Hum:{}% State:{}".format(moisture, temp_c, humidity_pct, state))

    conn, _ = server.accept()
    conn.recv(1024)
    response = dashboard_page(ip_address, moisture, temp_c, humidity_pct, state)
    conn.sendall(response.encode())
    conn.close()
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| `plant_state()` | Summarises the sensor data into a single farm condition | Dashboards are more useful when they show decisions, not just numbers |
| `dashboard_page()` | Builds an HTML page that shows the sensor dashboard | The page becomes the communication layer for the system |
| Auto-refresh meta tag | Reloads the dashboard page every five seconds | Students can watch live changes without manually refreshing |
| Shared Wi-Fi setup | Connects the Pico to the local network | No dashboard is possible until networking works reliably |

---

## Expected Result

A browser should load a simple dashboard page that refreshes automatically and shows soil moisture, temperature, humidity, and the current plant state. Changing the sensor conditions should eventually change the summary shown on the page.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The page never loads | Wrong IP address or viewing device is on a different network | Use the latest IP shown in Thonny and connect the viewing device to the same Wi-Fi network |
| The page loads but shows zeros | BME280 sensor not responding | Test the BME280 sensor separately and check the SDA and SCL wires |
| The plant state seems wrong | Thresholds are not tuned for the test environment | Tune the rule thresholds after observing real sensor values |
| The moisture value is unstable | ADC wiring is loose or calibration is wrong | Recheck the ADC wiring and capture new dry and wet values |

---

## Challenge Extensions

- Add an OLED mirror of the dashboard for local viewing without Wi-Fi
- Add a second page that shows raw values as well as the simplified state
- Add an automatic alert indicator when the state stays critical for several refresh cycles

---

## Reflection Questions

1. Why is a dashboard often easier to use than reading separate serial messages from multiple sensors?
2. Why should a dashboard include both raw readings and a simplified summary?
3. What is lost when a complex environment is reduced to a short state label like HOT AND DRY?
4. How would you redesign the page if this system had to monitor ten plant zones instead of one?

---

## Save Your Work

Save the file to your computer as:

```
project_132_iot_farm_dashboard.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 133: Crop Environment Logger**