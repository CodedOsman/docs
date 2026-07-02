# Project 207
## SANITATION MONITORING HUB

**Advanced Embedded Systems Project Using Raspberry Pi Pico 2 W and MicroPython**



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

The Pico records occupancy and odor-proxy conditions for a sanitation facility, then prepares local network reports for later dashboard use.

Facility management becomes reactive when usage and odor conditions are not logged in a consistent, reviewable way.

A Pico 2 W prototype with a PIR sensor, MQ-135 gas sensor, status LED, and Wi-Fi connection.

Edge-based usage counting, odor-proxy reporting, Wi-Fi upload structure, and honest prototype framing.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

Connected sanitation monitoring can support maintenance planning, but classroom builds should be described as local facility reporting prototype rather than finished remote platforms.

---

## Learning Objectives

- Combine sensing with Wi-Fi communication
- Validate local logging before trusting network upload
- Explain why a prototype endpoint is not a finished cloud platform
- Test sensor, communication, and fallback behavior separately
- Discuss data quality and deployment reliability

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board with Wi-Fi | Use MicroPython firmware |
| PIR motion sensor | 1 | Detects occupancy or usage events | Allow warm-up time before counting events |
| MQ-135 gas sensor module | 1 | Provides an odor or air-quality proxy | Warm up before use and protect the ADC if required |
| LED | 1 | Shows send or buffer state | Add a 220 ohm resistor |
| 2.4 GHz Wi-Fi network | 1 | Provides local network access | Use a local test network only |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses built-in MicroPython modules such as `network`, `socket`, and `ujson`.
- Enter your 2.4 GHz Wi-Fi network name and password in the code before testing the communication step.
- Set the local server IP address, port, and path in the code if you want the prototype to send data to a school or lab endpoint.
- This project demonstrates local sensing and data exchange only. It does not create a complete cloud platform by itself.
- This project demonstrates a local sanitation reporting node that could later feed a dashboard. It does not create a complete cloud platform by itself.

### Project-Specific Safety Note

Gas sensor readings are for learning and prototype use only and should not be treated as certified safety measurements.

Many MQ sensor modules use a 5V heater and can output up to 5V on the analog pin. Use a resistor divider or a 3.3V-safe conditioning board before connecting the analog output to the Pico ADC.

Public hygiene or compliance outputs in this project are prototype indicators only and should not replace trained human inspection.

The odor score is a prototype indicator only and should not be treated as a certified sanitation or health measurement.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| PIR OUT | GPIO 14 | GPIO 14 / physical pin 19 | Occupancy input |
| MQ-135 AO | GPIO 26 ADC0 | GPIO 26 / physical pin 31 | Odor proxy input |
| LED anode | 220 ohm resistor to GPIO 16 | GPIO 16 / physical pin 21 | Communication status LED |

---

## Wiring Diagram

```
  PIR OUT                     -> GPIO 14
  MQ-135 AO                   -> GPIO 26
  GPIO 16 -> 220 ohm resistor -> LED anode
  Common GND                  -> PIR, MQ-135, and LED
```

---

## Step-by-Step Assembly

1. Connect the PIR output to GPIO 14 and allow it to warm up before testing counts.
2. Connect the MQ-135 analog output to GPIO 26 through a safe ADC path.
3. Wire the LED to GPIO 16 through a 220 ohm resistor and connect the cathode to ground.
4. Enter the local Wi-Fi and server settings in the code before testing communication.
5. Warm up the MQ-135 and observe a baseline before choosing alert thresholds.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Test the PIR event counting and the MQ-135 reading separately before combining them.
3. **Test the output device**: Test the status LED and confirm the Wi-Fi code can connect to the local network.
4. **Test the decision logic**: Trigger occupancy events and odor changes separately so the report payload can be validated.
5. **Run the full system**: Run the full system and observe whether reports are sent or buffered locally.
6. **Validate the prototype**: Compare the recorded usage count with real observed visits to validate the event logic.
7. **Save the project**: Save the validated program on the Pico as main.py and keep a copy on the computer for future edits.

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE, copy and paste this code into a new file or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, Pin
import network
import socket
import time
import ujson

PIR_PIN = 14
GAS_PIN = 26
LED_PIN = 16
GAS_WATCH = 18000
GAS_SERVICE = 28000
WIFI_SSID = 'YOUR_WIFI'
WIFI_PASSWORD = 'YOUR_PASSWORD'
SERVER_HOST = '192.168.1.10'
SERVER_PORT = 8000
SERVER_PATH = '/facility'
BUFFER_FILE = 'sanitation_reports.log'
FACILITY_ID = 'RESTROOM_01'

pir = Pin(PIR_PIN, Pin.IN, Pin.PULL_DOWN)
gas_sensor = ADC(GAS_PIN)
led = Pin(LED_PIN, Pin.OUT)
usage_count = 0
occupied = False


def connect_wifi(timeout_seconds=12):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if wlan.isconnected():
        return wlan
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    start = time.time()
    while not wlan.isconnected() and time.time() - start < timeout_seconds:
        time.sleep(1)
    return wlan if wlan.isconnected() else None


def send_payload(payload):
    body = ujson.dumps(payload)
    try:
        addr = socket.getaddrinfo(SERVER_HOST, SERVER_PORT)[0][-1]
        client = socket.socket()
        client.settimeout(5)
        client.connect(addr)
        request = 'POST {} HTTP/1.1\r\nHost: {}\r\nContent-Type: application/json\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}'.format(SERVER_PATH, SERVER_HOST, len(body), body)
        client.send(request.encode())
        client.close()
        return True
    except OSError:
        return False


def buffer_payload(payload):
    with open(BUFFER_FILE, 'a') as handle:
        handle.write(ujson.dumps(payload) + '\n')


print('Sanitation reporting node ready')

while True:
    motion = pir.value() == 1
    if motion and not occupied:
        usage_count += 1
        occupied = True
    elif not motion:
        occupied = False

    gas_value = gas_sensor.read_u16()
    if gas_value >= GAS_SERVICE:
        state = 'SERVICE'
    elif gas_value >= GAS_WATCH:
        state = 'WATCH'
    else:
        state = 'NORMAL'

    payload = {
        'facility': FACILITY_ID,
        'timestamp': time.time(),
        'usage_count': usage_count,
        'gas_value': gas_value,
        'state': state,
    }

    wlan = connect_wifi()
    sent = False
    if wlan:
        sent = send_payload(payload)

    if sent:
        led.value(1)
        print('Sent {}'.format(payload))
    else:
        led.value(0)
        buffer_payload(payload)
        print('Buffered {}'.format(payload))

    time.sleep(5)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters | What to Modify During Testing |
|--------------|--------------|----------------|------------------------------|
| Edge-based counting | Counts a usage event only when motion first appears | Without edge logic, one visitor could be counted many times | Walk in and out several times to confirm the counter behaves realistically |
| Odor proxy state | Turns the MQ-135 reading into NORMAL, WATCH, or SERVICE | The state makes the report easier to understand than a raw gas value alone | Adjust thresholds only after observing warm-up and room baseline values |
| Upload with buffering | Attempts a local upload and falls back to a file if it fails | This keeps the prototype honest and useful even during network failures | Inspect the buffer file during testing to confirm fallback works |

---

## Expected Result

The serial monitor reports the current reading or state clearly.

The hardware output responds when the decision logic changes state.

Subsystem behavior matches the thresholds, timing, or rules described in the document.

### Validation Checks

- **Normal condition test**: confirm the system stays in its safe or idle state under baseline conditions
- **Warning condition test**: move the input close to the chosen threshold and confirm the transition is sensible
- **Critical condition test**: trigger the strongest alert or control state and confirm the output response is correct
- **Calibration test**: compare the sensor or timing against a known reference or repeated trial
- **Limitation test**: deliberately create an awkward or noisy condition and note how the prototype behaves

### Deployment and Limitations

- This prototype is suitable for local pilots where sensor data must be logged or transmitted over short periods
- Before deployment, network reliability, power backup, and endpoint security need attention
- The system should keep useful local behavior even when communication fails

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|---------|----------------|----------|
| Usage count rises too fast | The PIR warm-up or room placement is causing repeated triggers | Allow warm-up and aim the PIR at the entry path rather than the whole room |
| The state is always SERVICE | The gas sensor is still warming up or the thresholds are too low | Allow warm-up time and adjust thresholds after observing the baseline |
| Reports are never sent | The Wi-Fi or local endpoint settings are wrong | Verify the local network credentials and confirm the server is reachable |
| Every report is buffered | The upload socket request is failing | Test the endpoint separately and confirm the host, port, and path values |

---

## Challenge Extensions

- Add local storage buffering when the network is unavailable
- Add a dashboard or mobile notification layer
- Add encryption or authentication planning for real deployment
- Add battery or solar-power planning for field use

---

## Reflection Questions

1. What happens if the sensor is correct but the network is down?
2. How would you validate uploaded data against local data?
3. What privacy or safety issue appears when sending field data over Wi-Fi?
4. What would you improve before long-term deployment?

---

## Save Your Work

Save the file to your computer as:

```
project_207_sanitation_monitoring_hub.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 208: Public Washroom Alert**