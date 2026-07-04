# Project 123
## Wi-Fi Controlled Irrigation

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

This project builds a Wi-Fi irrigation controller that can be monitored and operated from a web browser on the same network.

Students will combine moisture sensing, timed pump control, automatic mode, manual browser commands, and Wi-Fi setup.

The final system should host a simple control page, show the current moisture percentage, and support manual watering while still allowing automatic operation.

### Project Story

The real-world use case is a classroom garden or greenhouse bench where a phone or laptop can trigger watering without touching the circuit.

---

## Learning Objectives

- Connect the Pico 2 W to a local Wi-Fi network
- Serve a simple HTML control page from MicroPython
- Combine manual browser commands with automatic threshold logic
- Use timed pump control and re-arm logic for safer irrigation behaviour
- Troubleshoot network setup and browser-based device control

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Wi-Fi capable controller | Use MicroPython |
| Soil moisture sensor | 1 | Analog soil input | Calibrate before testing auto mode |
| 1-channel relay module | 1 | Switches pump power | Verify active-low or active-high logic |
| Small DC water pump | 1 | Watering actuator | Use an external supply |
| External pump power supply | 1 | Pump power source | Match the pump voltage |
| LED and 220 Ω resistor | 1 each | Pump status indicator | Current-limited output only |
| Phone or computer | 1 | Browser-based controller | Must be on the same Wi-Fi network |
| Breadboard, jumper wires, tubing, and water container | 1 set | Prototype and test rig | Keep water away from the Pico |

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

Only expose this demo server on a trusted local network used for classroom testing.

Test the relay and browser buttons before connecting the live pump.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Soil sensor AOUT | GPIO 26 | GPIO 26 / physical pin 31 | ADC input |
| Relay IN | GPIO 15 | GPIO 15 / physical pin 20 | Pump control |
| Status LED anode | GPIO 16 through 220 Ω resistor | GPIO 16 / physical pin 21 | Pump activity indicator |
| Status LED cathode | GND | Any GND pin | LED return |
| Pump supply path | Relay COM to NO contacts | Not a Pico GPIO | External power only |

---

## Wiring Diagram

```
  Raspberry Pi Pico 2 W
  ┌─────────────────────┐
  │                     │
  │  GPIO 26 ───────────┤──── Soil Sensor AOUT
  │  GPIO 15 ───────────┤──── Relay IN
  │  GPIO 16 ────220Ω───┤──── LED (+)
  │                     │
  │  3.3V    ───────────┤──── Soil Sensor VCC
  │  GND     ───────────┤──── Soil Sensor GND
  │  GND     ───────────┤──── LED (-)
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

### Step 3: Connect Soil Sensor Power
Connect the soil sensor VCC pin to **3.3V**. Connect the soil sensor GND pin to **GND**.

### Step 4: Connect Soil Sensor AOUT
Connect the soil sensor AOUT, AO, or Signal pin to **GPIO 26** (ADC0).

### Step 5: Place and Wire the Relay Module
Identify relay VCC, GND, IN, COM, NO, and NC. Connect relay IN to **GPIO 15**. Power the relay module from the supply required by its label. Connect relay GND to Pico GND and to the external pump supply GND where shared grounding is required.

### Step 6: Place the Status LED
Place the status LED on the breadboard. Connect the long leg through a 220Ω resistor to **GPIO 16**. Connect the short leg to **GND**.

### Step 7: Wire the Pump Through the Relay
Connect the external pump supply positive wire to relay **COM**. Connect relay **NO** to the pump positive lead. Connect the pump negative lead to the external pump supply negative wire.

### Step 8: Prepare for Wi-Fi Testing
Keep the hardware wiring complete before opening the browser control page. Your phone or computer must be on the same Wi-Fi network as the Pico 2W.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Soil sensor VCC connects to 3.3V
- [x] Soil sensor GND connects to GND
- [x] Soil sensor AOUT / AO / Signal connects to GPIO 26
- [x] Relay IN connects to GPIO 15
- [x] Relay module uses the correct external supply and shared ground where required
- [x] Status LED long leg connects through a 220Ω resistor to GPIO 16
- [x] Status LED short leg connects to GND
- [x] Pump positive path uses relay COM and NO
- [x] Pump negative connects to external pump supply negative
- [x] Pico 2W and browser device are on the same Wi-Fi network for web control
- [x] No loose jumper wires

> **Intermediate Note**
> When running the networking part, the Pico 2W must be connected to Wi-Fi. Replace the SSID and PASSWORD placeholders in the MicroPython code before testing. Use the IP address shown in the Thonny Shell to open the local browser page. Test the relay and LED before connecting the live pump.

> **Safety Note**
> Do not power the pump from the Pico. Use an external pump supply, keep electronics away from water, and use the browser controls only while supervising the pump.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the sensor, LED, and relay wiring before any network testing
- Keep the pump disconnected until the browser control page is working

### Test the Input Sensor

- Run a short ADC script and record dry and wet sensor values
- Check that the calculated moisture percentage changes as the probe moves between dry and wet conditions

### Test the Output Device

- Verify the LED and relay switch correctly from a temporary test script
- Confirm the relay does not energise unexpectedly at boot

### Test Communication

- Upload the final code, wait for the IP address, and open it in a browser on the same Wi-Fi network
- Use the page buttons to test Water Once, Stop Pump, Auto Mode, and Manual Mode

### Run the Full System

- Reconnect the real pump and test one short manual watering cycle
- Enable auto mode and confirm that the pump only runs when the soil is dry and the rest timer has expired

### Save the Project

- Save the final code and note the IP address behaviour on your network
- Record the calibration values and thresholds that worked best in your test setup

### Additional Testing and Calibration Checks

**Calibration and tuning notes**

- Verify the Wi-Fi connection first before troubleshooting the web page buttons
- Use manual mode for the first live pump test so you can supervise the hardware closely
- If the page loads but the pump does not respond, test the relay path separately from the networking code
- Calibrate the soil sensor before trusting automatic watering decisions

**Quick testing checklist**

- [ ] Pico joins the Wi-Fi network and prints an IP address
- [ ] The browser page loads on a phone or computer on the same network
- [ ] Manual Water Once runs one timed cycle
- [ ] Stop Pump cancels an active cycle
- [ ] Auto Mode waters only when the moisture is below the dry threshold

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
status_led = Pin(16, Pin.OUT)

dry_reading = 52000
wet_reading = 22000
dry_threshold = 35
recovery_threshold = 45

auto_mode = True
ready_to_water = True
pump_running = False
pump_stop_at = 0
last_cycle = time.time() - MIN_REST_S

relay.value(RELAY_OFF)
status_led.value(0)


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def moisture_percent(raw_value):
    span = dry_reading - wet_reading
    if span == 0:
        return 0
    percent = int(((dry_reading - raw_value) * 100) / span)
    return clamp(percent, 0, 100)


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


def start_pump(reason):
    global pump_running, pump_stop_at, last_cycle, ready_to_water
    relay.value(RELAY_ON)
    status_led.value(1)
    pump_running = True
    pump_stop_at = time.time() + PUMP_RUN_S
    last_cycle = time.time()
    ready_to_water = False
    print("Pump ON:", reason)


def stop_pump(reason):
    global pump_running
    relay.value(RELAY_OFF)
    status_led.value(0)
    pump_running = False
    print("Pump OFF:", reason)


def html_page(ip_address, moisture):
    mode_text = "AUTO" if auto_mode else "MANUAL"
    pump_text = "ON" if pump_running else "OFF"
    return """HTTP/1.1 200 OK
Content-Type: text/html
Connection: close

<!DOCTYPE html>
<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Wi-Fi Irrigation</title>
<style>body{font-family:Arial;margin:20px;}button{padding:12px 18px;margin:6px;} .card{padding:12px;border:1px solid #ccc;border-radius:8px;margin-bottom:12px;}</style>
</head><body>
<h2>Wi-Fi Controlled Irrigation</h2>
<div class='card'>IP: {ip}<br>Moisture: {moisture}%<br>Mode: {mode}<br>Pump: {pump}</div>
<a href='/'><button>Refresh</button></a>
<a href='/water'><button>Water Once</button></a>
<a href='/stop'><button>Stop Pump</button></a>
<a href='/auto'><button>Enable Auto Mode</button></a>
<a href='/manual'><button>Manual Mode</button></a>
</body></html>""".format(ip=ip_address, moisture=moisture, mode=mode_text, pump=pump_text)


wlan = connect_wifi()
ip_address = wlan.ifconfig()[0]

server = socket.socket()
server.bind(("0.0.0.0", 80))
server.listen(1)
server.settimeout(0.2)

print("Open http://{}".format(ip_address))

while True:
    now = time.time()
    moisture = moisture_percent(soil.read_u16())

    if pump_running and now >= pump_stop_at:
        stop_pump("timed cycle complete")

    if moisture >= recovery_threshold:
        ready_to_water = True

    if auto_mode and ready_to_water and (not pump_running) and moisture <= dry_threshold and (now - last_cycle) >= MIN_REST_S:
        start_pump("automatic web-enabled cycle")

    try:
        conn, _ = server.accept()
    except OSError:
        time.sleep(0.1)
        continue

    request = conn.recv(1024)
    request_text = request.decode("utf-8", "ignore")

    if "GET /water" in request_text:
        auto_mode = False
        if not pump_running:
            start_pump("manual browser request")
    elif "GET /stop" in request_text:
        auto_mode = False
        if pump_running:
            stop_pump("manual stop request")
    elif "GET /auto" in request_text:
        auto_mode = True
    elif "GET /manual" in request_text:
        auto_mode = False

    response = html_page(ip_address, moisture)
    conn.sendall(response.encode())
    conn.close()
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| `connect_wifi()` | Connects the Pico to the local network with a timeout | Network failures are easier to diagnose when connection logic is explicit |
| `html_page()` | Builds the browser control page | The web page becomes the human interface for this IoT system |
| `start_pump()` and `stop_pump()` | Centralise timed pump control | One control path prevents conflicting pump states |
| `auto_mode` with browser routes | Separates automatic logic from manual web commands | Students can switch safely between autonomous and supervised operation |

---

## Expected Result

After connecting to Wi-Fi, the Pico should print an IP address in Thonny. Opening that address in a browser should show a simple irrigation page with the current moisture reading, the current mode, and the pump state. The Water Once button should trigger one timed watering cycle and Auto Mode should allow irrigation only when the soil is dry.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The browser cannot open the page | The phone and Pico are on different networks or the IP address changed | Reconnect both devices to the same Wi-Fi network and use the latest IP printed in Thonny |
| Buttons load the page but do not change the pump state | The relay path is wrong or the request route is not parsed as expected | Check the relay wiring and print the request text during debugging |
| Auto mode never waters | Thresholds are too low or the soil sensor is not calibrated | Recalibrate the sensor and compare the live moisture percentage with the soil condition |
| Pump stays on after a command | Timed stop logic is not being reached or the relay logic is reversed | Verify `PUMP_RUN_S`, confirm the main loop is still running, and check `RELAY_ON` / `RELAY_OFF` |

---

## Challenge Extensions

- Add a read-only JSON status endpoint for future mobile app integration
- Add a manual override lock so only one browser action is accepted during a pump cycle
- Add a low-water reservoir sensor so remote commands cannot start a dry pump

---

## Reflection Questions

1. Why is it useful to separate manual mode from automatic mode in a web-controlled system?
2. What new failure modes appear when you add networking to a simple irrigation controller?
3. Why should a remote control page still use timed pump cycles instead of an unlimited ON command?
4. How would you secure or simplify this project before using it outside the classroom?

---

## Save Your Work

Save the file to your computer as:

```
project_123_wifi_controlled_irrigation.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 124: Rain-Aware Irrigation**