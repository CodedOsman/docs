# Project 194
## ENVIRONMENTAL DATA CLOUD LOGGER

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

The Pico reads environmental sensor data, packages it into a local record, and tries to send the record to a local network endpoint.

Environmental data is harder to compare over time when readings are not stored or transmitted in a consistent format.

A Pico 2 W prototype with an MQ-5 Liquefied Petroleum/Methane Gas Sensor, BME280 environmental sensor, status LED, and Wi-Fi connection.

Local-first Wi-Fi logging, payload design, buffering, and realistic prototype framing.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

Connected environmental nodes are useful for monitoring trends, but classroom prototypes should describe them honestly as local logging or node demonstrations rather than as finished cloud platforms.

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
| MQ-5 Liquefied Petroleum/Methane Gas Sensor | 1 | Provides an LPG/methane gas proxy input | Warm up before use and protect the ADC if required |
| BME280 environmental sensor | 1 | Measures temperature, humidity, and pressure | Uses I2C; upload bme280.py if needed |
| LED | 1 | Shows upload or buffer activity | Add a 220 ohm resistor |
| 2.4 GHz Wi-Fi network | 1 | Provides local network access | Use a local test network only |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- Upload a compatible bme280.py MicroPython driver for BME280 readings. The network payload code uses built-in MicroPython modules such as network, socket, and ujson.
- Enter your 2.4 GHz Wi-Fi network name and password in the code before testing the communication step.
- Set the local server IP address, port, and path in the code if you want the prototype to send data to a school or lab endpoint.
- This project demonstrates local sensing and data exchange only. It does not create a complete cloud platform by itself.
- This environmental cloud logger is a local prototype node and not a complete cloud platform.

### Project-Specific Safety Note

Gas sensor readings are for learning and prototype use only and should not be treated as certified safety measurements.

Many MQ sensor modules use a 5V heater and can output up to 5V on the analog pin. Use a resistor divider or a 3.3V-safe conditioning board before connecting the analog output to the Pico ADC.

Validate the sensor readings locally first before evaluating the network upload behavior.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| BME280 VCC | 3.3V output | Physical pin 36 | Sensor power |
| BME280 GND | GND | Physical pin 38 | Common ground |
| BME280 SDA | GPIO 20 | GPIO 20 / physical pin 26 | I2C0 SDA |
| BME280 SCL | GPIO 21 | GPIO 21 / physical pin 27 | I2C0 SCL |
| MQ-5 AO | GPIO 26 ADC0 | GPIO 26 / physical pin 31 | LPG/methane gas proxy input |
| LED anode | 220 ohm resistor to GPIO 16 | GPIO 16 / physical pin 21 | Communication status LED |

---

## Step-by-Step Assembly

1. Connect the MQ-5 analog output to GPIO 26 through a safe ADC path.
2. Connect the BME280 to Pico 3.3V, GND, GPIO 20 (SDA), and GPIO 21 (SCL).
3. Wire the LED to GPIO 16 through a 220 ohm resistor and connect the cathode to ground.
4. Enter the Wi-Fi credentials and local server settings in the code before testing uploads.
5. Warm up the MQ-5 before trusting the environmental payload values.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Read and print both sensors locally before testing any network code.
3. **Test the output device**: Test the status LED separately, then test Wi-Fi connection without sending sensor data.
4. **Test the decision logic**: Trigger NORMAL and ALERT conditions and confirm the payload label changes logically.
5. **Run the full system**: Run the full logger and observe whether uploads succeed or records are buffered locally.
6. **Validate the prototype**: Disconnect the Wi-Fi intentionally to confirm the buffer fallback works.
7. **Save the project**: Save the validated program on the Pico as main.py and keep a copy on the computer for future edits.

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE, copy and paste this code into a new file or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, I2C, Pin
import bme280
import network
import socket
import time
import ujson

GAS_PIN = 26
BME_SDA_PIN = 20
BME_SCL_PIN = 21
LED_PIN = 16
GAS_WARN = 18000
GAS_ALERT = 28000
TEMP_WARN = 30
WIFI_SSID = 'YOUR_WIFI'
WIFI_PASSWORD = 'YOUR_PASSWORD'
SERVER_HOST = '192.168.1.10'
SERVER_PORT = 8000
SERVER_PATH = '/ingest'
BUFFER_FILE = 'env_buffer.log'
NODE_NAME = 'ENV_NODE_01'

mq5 = ADC(GAS_PIN)
i2c = I2C(0, sda=Pin(BME_SDA_PIN), scl=Pin(BME_SCL_PIN), freq=400000)
climate = bme280.BME280(i2c=i2c)
led = Pin(LED_PIN, Pin.OUT)


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
        request = 'POST {} HTTP/1.1\r\nHost: {}\r\nContent-Type: application/json\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}'.format(
            SERVER_PATH, SERVER_HOST, len(body), body)
        client.send(request.encode())
        client.close()
        return True
    except OSError:
        return False


def buffer_payload(payload):
    with open(BUFFER_FILE, 'a') as handle:
        handle.write(ujson.dumps(payload) + '\n')


print('Environmental Wi-Fi logger ready')

while True:
    gas_value = mq5.read_u16()
    try:
        values = climate.values
        temperature = float(values[0].replace('C', ''))
        pressure = float(values[1].replace('hPa', ''))
        humidity = float(values[2].replace('%', ''))
    except Exception:
        temperature = 0
        pressure = 0
        humidity = 0

    if gas_value >= GAS_ALERT:
        label = 'ALERT'
    elif gas_value >= GAS_WARN or temperature >= TEMP_WARN:
        label = 'WATCH'
    else:
        label = 'NORMAL'

    payload = {
        'node': NODE_NAME,
        'timestamp': time.time(),
        'gas': gas_value,
        'temperature_c': temperature,
        'humidity_percent': humidity,
        'label': label,
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
| Payload building | Turns sensor readings into a compact JSON record with a label | A clear payload structure supports later dashboards or analysis | Add or remove fields only after validating the local measurements |
| Wi-Fi connection | Attempts to join the configured 2.4 GHz network | Communication testing should be separated from sensor testing | Verify the SSID, password, and local network reachability if it never connects |
| Local buffer fallback | Stores the payload to a file if the network send fails | A realistic prototype should not discard data silently when the network is down | Delete or inspect the buffer file during testing to verify fallback behavior |

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
| Uploads never succeed | The Wi-Fi or server settings are wrong | Verify the SSID, password, host, port, and path against a local test server |
| Every record is buffered | The socket send is failing or the server is unreachable | Test on the same local network and confirm the endpoint is listening |
| Gas readings seem unrealistic | The MQ-5 is still warming up or the ADC path is unsafe | Allow warm-up time and confirm the analog signal is safe for 3.3V ADC input |
| The BME280 readings stay at zero | The sensor read is failing | Shorten the wiring and test the BME280 separately before retrying uploads |

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
project_194_environmental_data_cloud_logger.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 195: Smart Rainwater Harvesting System**