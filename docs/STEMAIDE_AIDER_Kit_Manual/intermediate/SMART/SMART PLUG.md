# Project 119
## SMART PLUG

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

This project demonstrates the logic of a smart plug using a BLE-controlled relay and a safe low-voltage test load.

A real smart plug would need certified mains hardware, proper enclosure design, fuse protection, and legal electrical compliance. This document keeps the build at safe low voltage only.

The final system should let the student turn the load on, turn it off, toggle it, or run it for a timed interval from a phone.

### Project Story

Students learn timed switching, manual override, and state reporting without using dangerous mains wiring in the classroom.

---

## Learning Objectives

- Use a relay to switch a low-voltage load remotely
- Implement auto-off timer logic for a switched load
- Track and report the current relay state
- Understand the difference between a classroom proof-of-concept and a real mains smart plug product
- Test load switching with safe low-voltage hardware only

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller with BLE support | Use MicroPython |
| 1-channel relay module | 1 | Low-voltage load switch | Use a 3.3V-safe control stage or proper driver |
| Low-voltage test load | 1 | Example: LED strip, 5V lamp module, or safe DC device | Do not use mains AC in this classroom build |
| External load power supply | 1 | Powers the load and relay module if required | Check voltage and polarity |
| Breadboard and jumper wires | 1 set | Control wiring | Keep load wires separate from control wires |
| Phone with BLE app | 1 | Wireless controller | Use a BLE UART-style app |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- Software Installation and Setup
- Safety Guidelines
- Breadboard Basics
- Reading Circuit Diagrams

### Project-Specific Setup Notes

- This project uses the Pico's built-in wireless module plus two helper files: `ble_uart.py` and `ble_advertising.py`
- Save `ble_uart.py` to the Pico root folder as `ble_uart.py`
- Save `ble_advertising.py` to the Pico root folder as `ble_advertising.py`
- In Thonny Shell, run `import os; print(os.listdir())` and confirm both helper files are visible on the Pico
- Communication Setup: install a BLE app such as nRF Connect, LightBlue, or another BLE UART terminal app on your phone
- Scan for the device name `AIDER_SmartPlug` after the Pico starts advertising
- **Do not** pair from the normal phone Bluetooth settings menu. Open the terminal app, scan, connect to the UART-style service, then send text commands from inside the app
- If Bluetooth does not work, restart the Pico and rescan from the terminal app before changing the wiring

### Project-Specific Safety Note

Do not power motors, pumps, relays, or fans directly from Pico GPIO pins. Use an external power supply for pumps, motors, relay coils, and fans when required. If the relay module is controlled by the Pico, connect Pico GND to the external supply GND unless the relay module is fully opto-isolated and wired correctly.

**This project is a low-voltage smart-plug prototype only. Do not connect mains wall power to the relay module.**

If you need a real smart plug, use certified mains-rated hardware, enclosure design, fuse protection, and qualified human supervision.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Relay IN | GPIO 16 | GPIO 16 / physical pin 21 | Control signal |
| Relay GND | Pico GND and external supply GND | Physical pin 38 for Pico GND | Shared ground unless the module is fully isolated |
| Relay VCC | External module supply if required | Not a Pico GPIO | Check the relay module requirement |
| External load supply positive | Relay COM to NO path | Not a Pico GPIO | Switch the positive path of the low-voltage load |
| Load negative | External load supply negative | Not a Pico GPIO | Do not route load current through the Pico |

---

## Wiring Diagram

```text
Raspberry Pi Pico 2 W
┌─────────────────────┐
│                     │
│  GPIO 16 ───────────┤──── Relay IN
│  GND ───────────────┤──── Relay GND
│                     │
└─────────────────────┘

Relay Module (External Power)
┌──────────────────┐
│ VCC ─── External supply +
│ GND ─── External supply - / Pico GND
│ COM ─── Load positive (from supply +)
│ NO  ─── Load positive (to device)
│ NC  ─── Unused
└──────────────────┘
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W

Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Place the Relay Module

Place the relay module beside the breadboard where the control pins and screw terminals are easy to reach. Identify VCC, GND, IN, COM, NO, and NC before wiring.

### Step 3: Connect Relay IN

Connect relay IN to GPIO 16.

### Step 4: Connect Relay GND

Connect relay GND to Pico GND and to the external load supply GND unless the relay module is fully isolated.

### Step 5: Connect Relay VCC

Connect relay VCC to the external supply voltage required by your relay module.

### Step 6: Wire the Load Positive Path

Connect the external load supply positive wire to relay COM. Connect relay NO to the positive side of the low-voltage load.

### Step 7: Connect the Load Negative Wire

Connect the load negative wire directly to the external supply negative wire.

### Step 8: Test With a Small Load First

Use a small low-voltage indicator load for the first test before trying a larger low-voltage device.

---

## Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Relay IN connects to GPIO 16
- [x] Relay VCC connects to the correct external relay supply
- [x] Relay GND, Pico GND, and external load supply GND share a common reference where required
- [x] Load positive path uses relay COM and NO
- [x] Load negative connects to external supply negative
- [x] No load current is routed through the Pico
- [x] No loose jumper wires

> **Intermediate Note**
>
> This project uses wireless UART on the Raspberry Pi Pico 2W. Use a terminal app such as nRF Connect, LightBlue, or another BLE UART terminal to connect to `AIDER_SmartPlug` and send commands. The code treats the relay module as active-low, so the relay may turn on when its input is driven LOW.

> **Safety Note**
>
> Use low-voltage DC loads only. Do not wire mains AC in this student project. Use a relay module that can be triggered by a 3.3V GPIO signal, or add a proper driver circuit.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware setup

- Build the relay control side first
- Keep the load side clearly separated and labelled as low voltage only

### Test the output device

- Use a safe LED or low-voltage lamp load first
- Confirm the relay turns the load on and off correctly before using timer mode

### Test timer behaviour

- Upload the final code and use the Shell messages to observe timed switching
- Verify that the load switches off automatically after the timer expires

### Test communication

- Connect to `AIDER_SmartPlug` from the BLE app
- Send `on`, `off`, `toggle`, `timer 10`, and `status` to verify the command set

### Run the full system

- Try manual control first
- Then try a timed run and confirm the load turns off automatically at the end of the countdown

### Save the project

- Save the working code
- Write a note in your engineering log that this build is a low-voltage prototype, not a mains product

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import Pin
import bluetooth
import time
from ble_uart import BLEUART

DEVICE_NAME = "AIDER_SmartPlug"
RELAY_ON = 0
RELAY_OFF = 1

relay = Pin(16, Pin.OUT)
ble = bluetooth.BLE()
ble.active(True)
uart = BLEUART(ble, name=DEVICE_NAME)

timer_active = False
timer_deadline = 0
command_queue = []


def send_line(message):
    print(message)
    uart.write((message + "\n").encode())


def on_rx(data):
    command = data.decode("utf-8").strip().lower()
    if command:
        command_queue.append(command)


def plug_on():
    relay.value(RELAY_ON)


def plug_off():
    relay.value(RELAY_OFF)


def plug_state():
    return "ON" if relay.value() == RELAY_ON else "OFF"


uart.on_rx(on_rx)
plug_off()
send_line("Bluetooth smart plug prototype ready")

while True:
    now = time.ticks_ms()

    if timer_active and time.ticks_diff(now, timer_deadline) >= 0:
        timer_active = False
        plug_off()
        send_line("Timer complete. Plug OFF")

    if command_queue:
        command = command_queue.pop(0)
        if command == "on":
            timer_active = False
            plug_on()
            send_line("Plug ON")
        elif command == "off":
            timer_active = False
            plug_off()
            send_line("Plug OFF")
        elif command == "toggle":
            if plug_state() == "ON":
                plug_off()
            else:
                plug_on()
            send_line("Plug {}".format(plug_state()))
        elif command.startswith("timer "):
            seconds = int(command.split()[1])
            plug_on()
            timer_active = True
            timer_deadline = time.ticks_add(now, seconds * 1000)
            send_line("Plug ON for {} seconds".format(seconds))
        elif command == "status":
            remaining = 0
            if timer_active:
                remaining = max(0, time.ticks_diff(timer_deadline, now) // 1000)
            send_line("Plug:{} TimerActive:{} Remaining:{}s".format(plug_state(), timer_active, remaining))
        elif command == "help":
            send_line("Commands: on, off, toggle, timer <seconds>, status, help")
        else:
            send_line("Unknown command. Send help.")

    time.sleep_ms(100)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| Low-voltage relay control | Switches the example load using active-low relay logic | Represents the behaviour of a smart plug without dangerous mains wiring |
| toggle and timer commands | Provide both instant switching and timed switching | Make the system more practical than a simple on/off relay |
| timer_active and timer_deadline | Track whether auto-off is enabled and when it should happen | Prevent the load from staying on unintentionally |
| status report | Returns the current load state and timer information | Useful for safe verification during testing |

---

## Expected Result

The phone can switch the low-voltage load on or off, toggle the load, or run it for a timed interval. After a timed run, the load turns off automatically.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| Load never turns on | Relay wiring or external supply wiring is wrong | Check the COM/NO path and the low-voltage load supply. |
| Timed run never ends | The timer command may not have been parsed correctly | Send status and verify the remaining time is decreasing. |
| Project feels unsafe for the intended application | The title suggests a real mains smart plug but the build is only a low-voltage proof-of-concept | Keep the classroom build low voltage and request human review before any mains-related redesign. |
| Phone cannot find the BLE device | The Pico is not advertising or the BLE helper files are missing | Confirm ble_uart.py and ble_advertising.py are saved on the Pico, restart the board, and scan again from nRF Connect or LightBlue. |
| Commands do not change the system state | The phone is connected to the wrong service or the command text is different from the expected command | Reconnect to the BLE UART service and send the exact command shown in the test section. |

---

## Challenge Extensions

- Engineering Challenge: add energy-use estimation by logging how long the load stays on
- Add a second manual local switch so the prototype can still operate without the phone
- Replace the simple timer with daily scheduling logic in a future project

---

## Reflection Questions

1. Why is it important to keep this classroom smart-plug project at low voltage only?
2. What safety features would a real mains smart plug need that are missing here?
3. Why is auto-off timing useful in load-control systems?

---

## Save Your Work

Save the file to your computer as:

```
project_119_smart_plug.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

Project 120: Emergency Notifier
