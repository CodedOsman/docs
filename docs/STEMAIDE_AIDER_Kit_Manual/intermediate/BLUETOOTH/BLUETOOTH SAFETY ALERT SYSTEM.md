# Project 108
## BLUETOOTH SAFETY ALERT SYSTEM

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

This project builds a BLE safety alert node around an analog hazard sensor and a buzzer alarm.
The Pico watches the sensor value, compares it against a threshold, and raises an alert when the reading enters an unsafe zone.
A similar structure could be used for classroom-safe gas, smoke, or flame-sensor demonstrations where threshold logic matters more than advanced machine learning.
The final system should show live sensor status, allow threshold tuning over BLE, and sound a brief buzzer warning when the threshold is crossed.

### Project Story

This project connects classroom electronics to a practical embedded-system problem. Learners will see how sensors, logic, outputs, and communication can work together in a real application.

---

## Learning Objectives

- Read an analog safety sensor and compare it with a threshold
- Use rule-based decision logic for alert generation
- Add a buzzer as a local alert output
- Tune the alert threshold after measuring a normal baseline value
- Understand the limits of prototype safety systems compared with certified real systems

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller with BLE support | Use MicroPython |
| Analog safety sensor | 1 | Example: gas, smoke, or flame-proxy sensor with a 3.3V-safe output | If your module outputs 5V on AOUT, use a voltage divider before GPIO 26 |
| Active buzzer | 1 | Local alert output | Use a small 3.3V-safe buzzer or add a driver |
| Breadboard | 1 | Build area | Keep sensor and buzzer wiring secure |
| Jumper wires | 8 or more | Connections | Label the sensor output wire clearly |
| Phone with BLE app | 1 | Wireless monitor device | Use a BLE UART-style app |

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
- Communication Setup: install a BLE app such as nRF Connect, LightBlue, or another BLE UART terminal app on your phone
- Scan for the device name `AIDER_SafetyAlert` after the Pico starts advertising
- **Do not** pair from the normal phone Bluetooth settings menu. Open the BLE app, scan, connect to the UART-style service, then send text commands from inside the app
- If Bluetooth does not work, restart the Pico and rescan from the BLE app before changing the wiring

### Project-Specific Safety Note

Do not test this project with dangerous flames, gas leaks, or unsafe chemicals. Warm-up and baseline behaviour vary between sensor modules. Treat this as a threshold-logic prototype, not a certified safety system.
If your sensor module uses 5V and exposes a 5V analog output, do not connect it directly to the Pico ADC pin.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Safety sensor VCC | 3.3V or module-safe supply | Physical pin 36 if 3.3V-safe | Follow the sensor documentation |
| Safety sensor GND | GND | Physical pin 38 | Common ground |
| Safety sensor analog output | GPIO 26 | GPIO 26 / physical pin 31 | Use a divider first if the sensor output can exceed 3.3V |
| Buzzer positive (+) | GPIO 18 | GPIO 18 / physical pin 24 | Local alert output |
| Buzzer negative (-) | GND | Physical pin 38 | Common ground |

---

## Wiring Diagram

![Circuit Diagram](../../assets/intermidiate/BLUETOOTH/BLUETOOTH SAFETY ALERT/circuit_1.png)

```text
Raspberry Pi Pico 2 W
┌─────────────────────┐
│                     │
│  GPIO 26 ───────────┤──── Safety sensor AOUT
│  GPIO 18 ───────────┤──── Buzzer (+)
│                     │
│  3.3V    ───────────┤──── Safety sensor VCC
│  GND     ───────────┤──── Safety sensor GND
│  GND     ───────────┤──── Buzzer (-)
│                     │
└─────────────────────┘
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W

Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Place the Safety Sensor Module

Place the safety sensor module where it can sense the test condition without pulling on the jumper wires. Check the printed labels and identify VCC, GND, and analog output such as AOUT, AO, or Signal.

### Step 3: Connect Sensor VCC

Connect sensor VCC to 3.3V or to the sensor-safe supply listed in the module documentation. Use a different supply only if the sensor output is confirmed safe for Pico GPIO.

### Step 4: Connect Sensor GND

Connect sensor GND to GND.

### Step 5: Connect the Analog Output

Connect the sensor analog output to GPIO 26 (ADC0). Use a voltage divider first if the sensor output can exceed 3.3V.

### Step 6: Place the Buzzer

Place the buzzer on the breadboard and identify its positive (+) and negative (-) pins.

### Step 7: Connect the Buzzer Positive Pin

Connect the buzzer positive (+) pin to GPIO 18.

### Step 8: Connect the Buzzer Negative Pin

Connect the buzzer negative (-) pin to GND.

### Step 9: Check the Signal Voltage

Before powering the Pico, confirm that the sensor signal going to GPIO 26 will stay within 0V to 3.3V.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Safety sensor VCC connects to a safe supply for the module
- [x] Safety sensor GND connects to GND
- [x] Safety sensor analog output connects to GPIO 26
- [x] Sensor output is confirmed 3.3V-safe before connecting to the Pico
- [x] Buzzer positive pin connects to GPIO 18
- [x] Buzzer negative pin connects to GND
- [x] No loose jumper wires

> **Intermediate Note**
>
> This project uses BLE on the Raspberry Pi Pico 2W. Use a BLE app such as nRF Connect, LightBlue, or a BLE UART terminal to connect to `AIDER_SafetyAlert` and send commands. Record a normal baseline reading first, then test the alert threshold with a safe classroom demonstration condition.

> **Safety Note**
>
> This project is a learning prototype and should not be treated as a certified safety instrument. Never connect a sensor output above 3.3V directly to a Pico GPIO pin.

---

## Testing Individual Components

### Hardware Setup

- Build the analog sensor and buzzer circuit carefully
- If the sensor needs warm-up time, allow it to stabilise before analysing readings

### Test the Input Sensor

- Run a short script that prints the raw ADC value every 0.5 seconds
- Record a normal baseline reading in a safe condition before setting the alert threshold

### Test the Output Device

- Run a brief buzzer test
- Confirm the buzzer works without leaving it on continuously

### Test Communication

- Connect to `AIDER_SafetyAlert` from the BLE app
- Send `status` and `read` to confirm the command interface works

### Run the Full System

- Set the threshold slightly above the safe baseline for a classroom demonstration
- Confirm the buzzer and BLE alert trigger only after the threshold is crossed
- Use `arm` and `disarm` to check whether the local alert can be silenced safely

### Save the Project

- Save the working code and write down the baseline and threshold readings you used
- Document the limitations of your sensor module so you do not overclaim the system capability

---

## Full Project Code

```python
from machine import ADC, Pin
import bluetooth
import time
from ble_uart import BLEUART

DEVICE_NAME = "AIDER_SafetyAlert"
ALARM_COOLDOWN_MS = 10000

sensor = ADC(26)
buzzer = Pin(18, Pin.OUT)
ble = bluetooth.BLE()
ble.active(True)
uart = BLEUART(ble, name=DEVICE_NAME)

threshold = 30000
alarm_enabled = True
last_alarm_ms = time.ticks_add(time.ticks_ms(), -ALARM_COOLDOWN_MS)
command_queue = []


def send_line(message):
    print(message)
    uart.write((message + "\n").encode())


def on_rx(data):
    command = data.decode("utf-8").strip().lower()
    if command:
        command_queue.append(command)


def beep_alarm():
    for _ in range(3):
        buzzer.on()
        time.sleep_ms(150)
        buzzer.off()
        time.sleep_ms(150)


uart.on_rx(on_rx)
send_line("Bluetooth safety alert ready")

while True:
    now = time.ticks_ms()
    raw_value = sensor.read_u16()

    if alarm_enabled and raw_value >= threshold and time.ticks_diff(now, last_alarm_ms) >= ALARM_COOLDOWN_MS:
        beep_alarm()
        send_line("ALERT! Sensor value {} crossed threshold {}".format(raw_value, threshold))
        last_alarm_ms = now

    if command_queue:
        command = command_queue.pop(0)
        if command in ("status", "read"):
            state = "ARMED" if alarm_enabled else "DISARMED"
            send_line("State:{} Raw:{} Threshold:{}".format(state, raw_value, threshold))
        elif command == "arm":
            alarm_enabled = True
            send_line("Alarm armed")
        elif command in ("silence", "disarm"):
            alarm_enabled = False
            buzzer.off()
            send_line("Alarm disarmed")
        elif command.startswith("threshold "):
            threshold = int(command.split()[1])
            send_line("Threshold set to {}".format(threshold))
        elif command == "help":
            send_line("Commands: status, read, arm, silence, disarm, threshold <value>, help")
        else:
            send_line("Unknown command. Send help.")

    time.sleep_ms(200)
```

---

## How the Code Works

- **Analog sensor read** — Measures the current hazard-sensor value on ADC0. This raw value is the basis for every decision.
- **threshold** — Stores the trigger level for the alert. Students can tune the threshold after observing the baseline.
- **Alarm cooldown** — Prevents the buzzer from triggering on every loop pass. Makes the alert more controlled and realistic.
- **BLE command interface** — Arms, disarms, reports status, and changes the threshold. Supports safe tuning without rewiring the circuit.

---

## Expected Result

The BLE app shows the live sensor value and current threshold. When the reading crosses the threshold while the system is armed, the buzzer sounds briefly and an alert message is sent over BLE.

---

## Troubleshooting

- **Sensor value never changes** — The sensor output is on the wrong pin or the module is not powered correctly. Check the sensor supply and the GPIO 26 analog connection.
- **Alarm triggers immediately** — The threshold is below the normal baseline. Measure the safe baseline again and raise the threshold.
- **The sensor module may not be Pico-safe** — The analog output could exceed 3.3V. Stop the test and add a voltage divider or use a confirmed 3.3V-safe module before reconnecting it.
- **Phone cannot find the BLE device** — The Pico is not advertising or the BLE helper files are missing. Confirm `ble_uart.py` and `ble_advertising.py` are saved on the Pico, restart the board, and scan again from nRF Connect or LightBlue.
- **Commands do not change the system state** — The phone is connected to the wrong service or the command text is different from the expected command. Reconnect to the BLE UART service and send the exact command shown in the test section.

---

## Challenge Extensions

- Engineering Challenge: add a second threshold so the system reports WARNING before it reaches ALERT
- Store the last five raw readings and send the moving average instead of only the latest value
- Add an LED indicator with green, yellow, and red states based on the reading range

---

## Reflection Questions

1. Why is baseline testing important before choosing a safety threshold?
2. Why should this project be described as rule-based logic instead of full machine learning?
3. What extra hardware or certification would be required before using a real safety system in public spaces?

---

## Save Your Work

Save the file to your computer as:

- `project_108_bluetooth_safety_alert_system.py`

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

- `main.py`

---

## Next Project

Project 109: Bluetooth Remote Controlled Fan
