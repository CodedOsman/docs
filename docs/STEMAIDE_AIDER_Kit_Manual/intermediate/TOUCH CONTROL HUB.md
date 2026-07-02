# Project 112
## TOUCH CONTROL HUB

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

This project builds a touch-driven control hub that cycles through multiple output scenes and also accepts BLE commands.

A touch sensor acts as a local interface while the phone app provides remote scene selection and status checks.

The same control-hub idea can be reused for lighting scenes, kiosk controls, or simple interactive prototypes.

The final system should let a touch input cycle through OFF, LED 1, LED 2, and BOTH ON scenes while a phone can request or change the current scene over BLE.

### Project Story

This project connects classroom electronics to a practical embedded-system problem. Learners will see how sensors, logic, outputs, and communication can work together in one system.

---

## Learning Objectives

- Use one touch input to control several output states
- Build a simple state machine for scene control
- Combine local control and remote BLE control
- Apply debounce timing to touch-sensor inputs
- Test the input and output devices separately before the full scene logic

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller with BLE support | Use MicroPython |
| Touch sensor module (TTP223 or similar) | 1 | Local touch input | Use 3.3V power for Pico-safe logic |
| LEDs | 2 | Scene outputs | Each LED needs its own resistor |
| 220Ω resistors | 2 | LED current limiters | Required for LED safety |
| Breadboard and jumper wires | 1 set | Connections | Keep touch sensor wires short |
| Phone with BLE app | 1 | Wireless scene controller | Use a BLE UART-style app |

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
- In Thonny Shell, run `import os; print(os.listdir())` and confirm both BLE helper files are visible on the Pico
- Communication Setup: install a BLE app such as nRF Connect, LightBlue, or another BLE UART terminal app on your phone
- Scan for the device name `AIDER_TouchHub` after the Pico starts advertising
- **Do not** pair from the normal phone Bluetooth settings menu. Open the BLE app, scan, connect to the UART-style service, then send text commands from inside the app
- If Bluetooth does not work, restart the Pico and rescan from the BLE app before changing the wiring

### Project-Specific Safety Note

Power the touch sensor from 3.3V so the output logic stays Pico-safe. Each LED must have its own resistor.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Touch sensor VCC | 3.3V | Physical pin 36 | Sensor power |
| Touch sensor GND | GND | Physical pin 38 | Common ground |
| Touch sensor SIG | GPIO 4 | GPIO 4 / physical pin 6 | Digital touch signal |
| LED 1 anode (+) | 220Ω resistor then GPIO 16 | GPIO 16 / physical pin 21 | Scene output 1 |
| LED 2 anode (+) | 220Ω resistor then GPIO 17 | GPIO 17 / physical pin 22 | Scene output 2 |
| LED 1 and LED 2 cathodes (-) | GND | Physical pin 38 | Common ground |

---

## Wiring Diagram

```text
Raspberry Pi Pico 2 W
┌─────────────────────┐
│                     │
│  GPIO 4  ───────────┤──── Touch sensor SIG
│  3.3V  ─────────────┤──── Touch sensor VCC
│  GND   ─────────────┤──── Touch sensor GND
│  GPIO 16 ───────────┤──── LED 1 through 220Ω
│  GPIO 17 ───────────┤──── LED 2 through 220Ω
│  GND   ─────────────┤──── LED cathodes
│                     │
└─────────────────────┘
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W

Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Place the Touch Sensor

Place the touch sensor where it can be tapped easily during testing. Check the printed labels and identify VCC, GND, and SIG before wiring.

### Step 3: Connect Touch Sensor VCC

Connect touch sensor VCC to 3.3V.

### Step 4: Connect Touch Sensor GND

Connect touch sensor GND to GND.

### Step 5: Connect Touch Sensor SIG

Connect touch sensor SIG to GPIO 4.

### Step 6: Place the Two LEDs

Place LED 1 and LED 2 on the breadboard. For each LED, identify the long leg as the anode (+) and the short leg as the cathode (-).

### Step 7: Connect LED 1 to GPIO 16

Connect LED 1 anode to one end of a 220Ω resistor. Connect the other end of the resistor to GPIO 16.

### Step 8: Connect LED 2 to GPIO 17

Connect LED 2 anode to one end of a 220Ω resistor. Connect the other end of the resistor to GPIO 17.

### Step 9: Connect the LED Cathodes

Connect both LED cathodes to GND.

---

## Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Touch sensor VCC connects to 3.3V
- [x] Touch sensor GND connects to GND
- [x] Touch sensor SIG connects to GPIO 4
- [x] LED 1 anode connects through a 220Ω resistor to GPIO 16
- [x] LED 2 anode connects through a 220Ω resistor to GPIO 17
- [x] Both LED cathodes connect to GND
- [x] No loose jumper wires

> **Intermediate Note**
>
> This project uses BLE on the Raspberry Pi Pico 2W. Use a BLE app such as nRF Connect, LightBlue, or a BLE UART terminal to connect to `AIDER_TouchHub` and send commands. The touch input changes the local scene outputs, and BLE commands can also report or control the scene state.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware setup

- Build the touch sensor and two LED outputs
- Place the touch sensor where it can be pressed or tapped easily during testing

### Test the input sensor

- Run a short script that prints `touch.value()` when the pad is touched
- Confirm the sensor changes state reliably and does not flicker too much

### Test the output devices

- Turn each LED on separately with a short script
- Fix any wiring issue before testing the scene logic

### Test communication

- Connect to `AIDER_TouchHub` from the BLE app
- Send `status`, `next`, and `scene 3` to verify the command set

### Run the full system

- Touch the sensor several times and confirm the scene cycles through OFF, LED1, LED2, and BOTH
- Use BLE commands to change the scene remotely and compare the response with local touch control

### Save the project

- Save the working scene-control code
- Record which scene order feels most intuitive for the user

---

## Full Project Code

```python
from machine import Pin
import bluetooth
import time
from ble_uart import BLEUART

DEVICE_NAME = "AIDER_TouchHub"
DEBOUNCE_MS = 300

touch = Pin(4, Pin.IN)
led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)

ble = bluetooth.BLE()
ble.active(True)
uart = BLEUART(ble, name=DEVICE_NAME)

scene_index = 0
last_touch_ms = 0
last_touch_state = 0
command_queue = []


def send_line(message):
    print(message)
    uart.write((message + "\n").encode())


def on_rx(data):
    command = data.decode("utf-8").strip().lower()
    if command:
        command_queue.append(command)


def apply_scene(index):
    global scene_index
    scene_index = index % 4
    if scene_index == 0:
        led1.off()
        led2.off()
    elif scene_index == 1:
        led1.on()
        led2.off()
    elif scene_index == 2:
        led1.off()
        led2.on()
    else:
        led1.on()
        led2.on()


def scene_name():
    names = ["OFF", "LED1", "LED2", "BOTH"]
    return names[scene_index]


uart.on_rx(on_rx)
apply_scene(0)
send_line("Bluetooth touch hub ready")

while True:
    now = time.ticks_ms()
    touch_state = touch.value()
    if touch_state == 1 and last_touch_state == 0 and time.ticks_diff(now, last_touch_ms) >= DEBOUNCE_MS:
        apply_scene(scene_index + 1)
        last_touch_ms = now
        send_line("Touch scene changed to {}".format(scene_name()))

    if command_queue:
        command = command_queue.pop(0)
        if command == "next":
            apply_scene(scene_index + 1)
            send_line("Scene changed to {}".format(scene_name()))
        elif command.startswith("scene "):
            apply_scene(int(command.split()[1]))
            send_line("Scene changed to {}".format(scene_name()))
        elif command == "status":
            send_line("Current scene: {}".format(scene_name()))
        elif command == "help":
            send_line("Commands: next, scene 0, scene 1, scene 2, scene 3, status, help")
        else:
            send_line("Unknown command. Send help.")

    last_touch_state = touch_state
    time.sleep_ms(80)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| `scene_index` | Stores which scene is active | This is the heart of the state-machine approach |
| `apply_scene()` | Updates both LEDs based on one scene number | Keeps the output logic organised and reusable |
| Touch edge detection | Looks for a new touch instead of a held touch | Stops one press from skipping through many scenes |
| BLE scene commands | Let the phone select or advance scenes | Show how one system can support both local and remote control |

---

## Expected Result

Each touch advances the system through OFF, LED1, LED2, and BOTH ON scenes. The phone can also request status or change the current scene through BLE commands.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| Touch input does nothing | The sensor is not powered or the signal wire is on the wrong pin | Check 3.3V, GND, and GPIO 4 wiring. |
| Scenes skip too quickly | Debounce time is too short or the touch is noisy | Increase `DEBOUNCE_MS` and retest. |
| One LED never changes | The LED channel or resistor path is broken | Recheck the GPIO 16 or GPIO 17 wiring for that LED. |
| Phone cannot find the BLE device | The Pico is not advertising or the BLE helper files are missing | Confirm `ble_uart.py` and `ble_advertising.py` are saved on the Pico, restart the board, and scan again from nRF Connect or LightBlue. |
| Commands do not change the system state | The phone is connected to the wrong service or the command text is different from the expected command | Reconnect to the BLE UART service and send the exact command shown in the test section. |

---

## Challenge Extensions

- Engineering Challenge: replace the LEDs with a relay pair or an RGB indicator and keep the same scene logic
- Add long-touch behaviour for a special scene or system reset
- Store the last scene so the hub can restore it after a reset

---

## Reflection Questions

1. Why is a state machine useful when one input controls several outputs?
2. Why might a touch interface behave differently from a push button?
3. Where would a touch-and-BLE control hub be more useful than a simple single-button system?

---

## Save Your Work

Save the file to your computer as:

```
project_112_touch_control_hub.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

Project 113: Multi Sensor Dashboard
