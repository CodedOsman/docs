# Project 134
## AUTOMATED IRRIGATION ALERTS

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

This project adds event-style alerts to an automatic irrigation system so watering activity can be reviewed from a browser as well as locally on the hardware.

Students will combine soil sensing, automatic pump control, a buzzer alert, a status LED, and a Wi-Fi event page.

The final system should start watering automatically when the soil is dry, record recent irrigation events, and show the alert history on a browser page over Wi-Fi.

### Project Story

The real-world use case is a plant station where the operator wants a short event history instead of watching the pump continuously.

---

## Learning Objectives

- Build a simple event log for an automated system
- Combine local alerts and Wi-Fi status reporting in one project
- Use a short buzzer pattern only when a meaningful irrigation event occurs
- Serve a browser page that shows the most recent system alerts
- Think about why event history helps troubleshooting in real automation systems

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Wi-Fi capable controller | Use MicroPython |
| Soil moisture sensor | 1 | Analog moisture input | Calibrate before final testing |
| 1-channel relay module | 1 | Switches pump power | Verify active-low or active-high logic |
| Small DC water pump | 1 | Watering output | Use an external power supply |
| External power supply | 1 | Pump and relay power source | Match the pump rating |
| Buzzer | 1 | Local alert output | Use short beeps only |
| LED and 220 Ω resistor | 1 each | Alert indicator | Current-limited output only |
| Phone or computer | 1 | Browser page viewer | Must be on the same Wi-Fi network |

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
- No external library is required. This project uses the built-in `network` and `socket` modules

### Project-Specific Safety Note

Do not power motors, pumps, fans, valves, or relay coils directly from Pico GPIO pins.

Use an external power supply for pumps, motors, relay modules, and fans when required.

If the relay module is controlled by the Pico, connect Pico GND to the external supply GND unless the relay module is fully opto-isolated and wired correctly.

Check whether your relay module is active-low or active-high before testing the final load.

Keep electronics away from water and dry your hands before touching the circuit.

Do not let exposed jumper connections touch water.

Do not let a pump run dry.

Use short buzzer alerts so the sound remains informative instead of distracting.

Do not assume the web page replaces direct supervision during the first live pump tests.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Soil sensor AOUT | GPIO 26 | GPIO 26 / physical pin 31 | ADC input |
| Relay IN | GPIO 15 | GPIO 15 / physical pin 20 | Pump control |
| Buzzer positive | GPIO 16 | GPIO 16 / physical pin 21 | Short alert tones |
| Alert LED anode | GPIO 17 through 220 Ω resistor | GPIO 17 / physical pin 22 | Lights when the pump is active |
| Alert LED cathode | GND | Any GND pin | LED return |
| Pump supply path | Relay COM to NO contacts | Not a Pico GPIO | External power only |

---

## Wiring Diagram

```
  Raspberry Pi Pico 2 W
  ┌─────────────────────┐
  │                     │
  │  GPIO 26 ───────────┤──── Soil Sensor AOUT
  │                     │
  │  GPIO 15 ───────────┤──── Relay IN
  │  GPIO 16 ───────────┤──── Buzzer (+)
  │  GPIO 17 ────220Ω───┤──── Alert LED (+)
  │                     │
  │  3.3V    ───────────┤──── Soil Sensor VCC
  │  GND     ───────────┤──── Soil Sensor GND
  │  GND     ───────────┤──── Buzzer (-)
  │  GND     ───────────┤──── Alert LED (-)
  │  GND     ───────────┤──── Relay GND
  │                     │
  └─────────────────────┘

  Relay Module            External Supply
  ┌──────────┐            ┌────────────┐
  │  COM ────┼────────────┤ (+)        │
  │  NO  ────┼──┐         │            │
  │  VCC ────┼──┼─────────┤ (+) (if    │
  │  GND ────┼──┼──┐      │   needed)  │
  └──────────┘  │  │      │            │
                │  │      └────────────┘
                │  │           │
                │  └───────────┘
                │         Pump (+)
                │
                └────────────── Pump (-) ──── External Supply (-)
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W
Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Position the Soil Moisture Sensor
Place the soil moisture probe so the sensing end can enter the soil sample. Identify VCC, GND, and AOUT / AO / Signal before wiring.

### Step 3: Connect the Soil Sensor
Connect soil sensor VCC to **3.3V**. Connect soil sensor GND to **GND**. Connect soil sensor AOUT, AO, or Signal to **GPIO 26** (ADC0).

### Step 4: Place and Wire the Relay Module
Identify relay VCC, GND, IN, COM, NO, and NC. Connect relay IN to **GPIO 15**. Power the relay module from the supply required by its label. Connect relay GND to Pico GND and to the external pump supply GND where shared grounding is required.

### Step 5: Place the Buzzer
Place the buzzer on the breadboard and identify its positive (+) and negative (-) pins. Connect the buzzer positive pin to **GPIO 16**. Connect the buzzer negative pin to **GND**.

### Step 6: Place the Alert LED
Place the alert LED on the breadboard. Connect its long leg through a 220Ω resistor to **GPIO 17**. Connect its short leg to **GND**.

### Step 7: Wire the Pump Through the Relay
Connect the external pump supply positive wire to relay **COM**. Connect relay **NO** to the pump positive lead. Connect the pump negative lead to the external pump supply negative wire.

### Step 8: Prepare for Wi-Fi Testing
Keep the pump wiring supervised before opening the browser page. Your phone or computer must be on the same Wi-Fi network as the Pico 2W.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Soil sensor AOUT / AO / Signal connects to GPIO 26
- [x] Relay IN connects to GPIO 15
- [x] Buzzer positive pin connects to GPIO 16
- [x] Buzzer negative pin connects to GND
- [x] Alert LED long leg connects through a 220Ω resistor to GPIO 17
- [x] Alert LED short leg connects to GND
- [x] Pump positive path uses relay COM and NO
- [x] Pump negative connects to external pump supply negative
- [x] Pico 2W is connected to Wi-Fi for the browser alert page
- [x] No loose jumper wires

> **Intermediate Note**
> When running the networking part, the Pico 2W must be connected to Wi-Fi. Replace the SSID and PASSWORD placeholders in the MicroPython code before testing. Test dry and wet soil readings before relying on alert thresholds. The relay code is active-low, so confirm the relay behavior before connecting the pump.

> **Safety Note**
> Do not power the pump from the Pico. Use short buzzer alerts, keep electronics away from water, and do not treat the web page as a replacement for supervising the first pump tests.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the sensor, buzzer, LED, and relay stage before enabling the network page
- Keep the pump disconnected until the alert logic is behaving as expected

### Test the Input Sensor

- Calibrate the soil sensor and compare the live moisture percentage with dry and wet conditions
- Confirm that the dry threshold is reachable during a simple classroom test

### Test the Output Device

- Verify that the buzzer and LED respond correctly during a short manual trigger or temporary threshold adjustment
- Test the relay separately before connecting the live pump

### Test Communication

- Connect the Pico to Wi-Fi and open the alert page in a browser on the same network
- Confirm that new event messages appear when the system becomes ready and when watering starts or stops

### Run the Full System

- Reconnect the real pump and allow one dry-soil watering event
- Check the browser page history and the local buzzer/LED response together

### Save the Project

- Save the final code and note the alert count and threshold values from your test
- Record how often the event page refreshed reliably on your network

### Additional Testing and Calibration Checks

**Calibration and tuning notes**

- Use a temporarily higher dry threshold to force one alert cycle during classroom testing
- Open the browser page before the dry test so you can watch the event list update live
- If the pump hardware is not connected yet, test the alert logic with the relay and LED only
- Check that the event list does not grow forever; the project should keep only a short recent history

**Quick testing checklist**

- [ ] Soil moisture values respond correctly to dry and wet conditions
- [ ] Buzzer and LED activate when a watering event begins
- [ ] Browser page loads on the same Wi-Fi network
- [ ] Recent events appear on the page
- [ ] The pump stops after the timed cycle completes

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
import network
import socket
import time
from machine import ADC, Pin

SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

RELAY_ON = 0
RELAY_OFF = 1
PUMP_RUN_S = 5
MIN_REST_S = 30

soil = ADC(26)
relay = Pin(15, Pin.OUT)
buzzer = Pin(16, Pin.OUT)
alert_led = Pin(17, Pin.OUT)

dry_reading = 52000
wet_reading = 22000
dry_threshold = 35
recovery_threshold = 45

ready_to_water = True
last_cycle = time.time() - MIN_REST_S
pump_running = False
pump_stop_at = 0
alert_count = 0
events = []

relay.value(RELAY_OFF)
buzzer.value(0)
alert_led.value(0)


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


def add_event(message):
    global alert_count
    stamp = time.time()
    entry = "{} | {}".format(int(stamp), message)
    events.append(entry)
    if len(events) > 8:
        events.pop(0)
    alert_count += 1
    print(entry)


def beep_once():
    buzzer.on()
    time.sleep(0.15)
    buzzer.off()


def start_pump(reason):
    global pump_running, pump_stop_at, last_cycle, ready_to_water
    relay.value(RELAY_ON)
    pump_running = True
    pump_stop_at = time.time() + PUMP_RUN_S
    last_cycle = time.time()
    ready_to_water = False
    alert_led.value(1)
    add_event("Watering started: {}".format(reason))
    beep_once()


def stop_pump(reason):
    global pump_running
    relay.value(RELAY_OFF)
    pump_running = False
    alert_led.value(0)
    add_event("Watering stopped: {}".format(reason))


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


def alert_page(ip_address, moisture):
    lines = "<br>".join(events[-5:]) if events else "No alerts yet"
    return """HTTP/1.1 200 OK
Content-Type: text/html
Connection: close

<!DOCTYPE html>
<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
<meta http-equiv='refresh' content='5'><title>Irrigation Alerts</title>
<style>body{font-family:Arial;margin:20px;} .card{padding:12px;border:1px solid #ccc;border-radius:8px;margin-bottom:12px;}</style>
</head><body>
<h2>Automated Irrigation Alerts</h2>
<div class='card'>IP: {ip}<br>Moisture: {moisture}%<br>Pump: {pump}<br>Alert count: {count}</div>
<div class='card'><strong>Recent events</strong><br>{events}</div>
</body></html>""".format(
        ip=ip_address,
        moisture=moisture,
        pump="ON" if pump_running else "OFF",
        count=alert_count,
        events=lines,
    )


wlan = connect_wifi()
ip_address = wlan.ifconfig()[0]

server = socket.socket()
server.bind(("0.0.0.0", 80))
server.listen(1)
server.settimeout(0.2)

print("Open http://{}".format(ip_address))
add_event("System ready")

while True:
    now = time.time()
    moisture = soil_percent()

    if moisture >= recovery_threshold:
        ready_to_water = True

    if pump_running and now >= pump_stop_at:
        stop_pump("timed cycle complete")

    if ready_to_water and (not pump_running) and moisture <= dry_threshold and (now - last_cycle) >= MIN_REST_S:
        start_pump("soil below dry threshold")

    try:
        conn, _ = server.accept()
    except OSError:
        time.sleep(0.1)
        continue

    conn.recv(1024)
    response = alert_page(ip_address, moisture)
    conn.sendall(response.encode())
    conn.close()
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| `events` list and `add_event()` | Store a short event history | Past alerts help explain what the system did |
| `start_pump()` and `stop_pump()` | Tie actuator control to event logging | Every important action becomes visible locally and on the page |
| `alert_page()` | Builds the browser event-history page | The Wi-Fi page is the communication layer of the project |
| `beep_once()` | Adds a short local audio alert | Local feedback is useful even if no browser is open |

---

## Expected Result

When the soil is dry enough, the system should start one timed watering cycle, beep briefly, light the LED, and add new messages to the browser alert page. The page should also keep a short history of recent events so students can see what happened in the last few cycles.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The event page is empty | The page is loading before the system logs any events | Wait for the startup message or trigger a test event by adjusting the threshold |
| The LED lights but the pump does not run | The relay path or external power wiring is wrong | Test the relay path separately and confirm the pump power supply |
| The buzzer keeps sounding | The alert logic is being retriggered repeatedly | Check the re-arm logic, recovery threshold, and rest timer |
| The browser page does not update | The device is on a different network or the IP changed | Use the latest IP address shown in Thonny and keep the viewer on the same Wi-Fi network |

---

## Challenge Extensions

- Add a manual acknowledge button on the page for future versions
- Add a reservoir-empty alert so the event log distinguishes watering from water-source faults
- Add CSV logging so the event history can be saved after power loss

---

## Reflection Questions

1. Why is an event log often more useful than only a live sensor value?
2. Why should local buzzer feedback and remote page feedback agree with each other?
3. What irrigation problems might still happen even if the event page looks correct?
4. How would you prevent alert fatigue if this system ran in a busy greenhouse?

---

## Save Your Work

Save the file to your computer as:

```
project_134_automated_irrigation_alerts.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 135: Smart Fertilizer Reminder**