# Project 103
# BLUETOOTH SMART SWITCH PANEL

Intermediate Embedded Systems Project Using Raspberry Pi Pico 2 W and MicroPython

- **Manual Section:** Intermediate Projects
- **Project Level:** Intermediate
- **Board:** Raspberry Pi Pico 2 W
- **Programming Language:** MicroPython
- **Version:** 1.0
- **Date:** May 2026
- **Prepared for:** STEMAIDE Africa

---

## Contents

- Overview
- Learning Objectives
- Required Components
- Before You Begin
- Circuit Connections
- Wiring Diagram
- Step-by-Step Assembly
- Testing Individual Components
- Full Project Code
- How the Code Works
- Expected Result
- Troubleshooting
- Challenge Extensions
- Reflection Questions
- Save Your Work
- Next Project

---

## Overview

This project creates a single-channel BLE switch panel that lets a phone control one relay output.
It demonstrates multi-output command parsing, shared system power rules, and safe low-voltage relay wiring.
The final system should let the student connect from a BLE app, switch the relay independently, and request a clear status report.

**Project Story**

A real-world version could be used to switch irrigation valves, greenhouse lights, or one low-voltage load from one controller.

---

## Learning Objectives

- Control multiple outputs from one BLE command interface
- Use active-low relay logic that matches many classroom relay modules
- Understand the difference between relay control wiring and load wiring
- Apply safe low-voltage switching rules before attempting any real actuator project
- Report system state clearly so testing and troubleshooting are easier

---

## Required Components

- **Raspberry Pi Pico 2 W** — Quantity: 1 — Main controller — *Important Note: Use MicroPython*
- **1-channel relay module** — Quantity: 1 — Switching interface for one load — *Important Note: Use only a 3.3V-safe input relay module or a proper driver stage*
- **Low-voltage test load** — Quantity: 1 — Example load such as an LED module or 5V lamp module — *Important Note: Do not use mains AC in this classroom build*
- **External 5V supply for relay/load side** — Quantity: 1 — Powers the relay module and test load — *Important Note: Check polarity before power-up*
- **Breadboard or terminal block area** — Quantity: 1 — For the control wiring — *Important Note: Keep control side separate from load side*
- **Jumper wires** — Quantity: 1 set — Connections — *Important Note: Label the relay control and load wires clearly*

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- Software Installation and Setup.
- Safety Guidelines.
- Breadboard Basics.
- Reading Circuit Diagrams.

**Project-Specific Setup Notes**

- These Bluetooth projects use the built-in bluetooth module plus two helper files: `ble_uart.py` and `ble_advertising.py`
- Save `ble_uart.py` to the Pico root folder as `ble_uart.py`
- Save `ble_advertising.py` to the Pico root folder as `ble_advertising.py`
- In Thonny Shell, run `import os; print(os.listdir())` and confirm both BLE helper files are visible on the Pico
- Communication Setup: install a BLE app such as nRF Connect, LightBlue, or another BLE UART terminal app on your phone
- Scan for the device name `AIDER_SwitchPanel` after the Pico starts advertising
- Do not pair from the normal phone Bluetooth settings menu. Open the BLE app, scan, connect to the UART-style service, then send text commands from inside the app
- If Bluetooth does not work, restart the Pico and rescan from the BLE app before changing the wiring

**Project-Specific Safety Note**

Do not power motors, pumps, relays, or fans directly from Pico GPIO pins.
Use an external power supply for pumps, motors, relay coils, and fans when required.
If the relay module is controlled by the Pico, connect Pico GND to the external supply GND unless the relay module is fully opto-isolated and wired correctly.
This project is a low-voltage demonstration only. Do not connect mains electricity to the relay module.
Test the relay outputs first with safe low-voltage indicator loads before trying any larger device.

---

## Circuit Connections

- **Relay module VCC** — Connects To: External 5V supply positive — Pico GPIO / Physical Pin Number: Not a Pico GPIO — *Notes: Power the relay module from the correct supply recommended for the module*
- **Relay module GND** — Connects To: External 5V supply GND and Pico GND — Pico GPIO / Physical Pin Number: Physical pin 38 for Pico GND — *Notes: Shared ground unless the module is fully isolated*
- **Relay IN** — Connects To: GPIO 16 — Pico GPIO / Physical Pin Number: GPIO 16 / physical pin 21 — *Notes: Single relay channel control*
- **Load positive path** — Connects To: Relay COM to NO path — Pico GPIO / Physical Pin Number: Not a Pico GPIO — *Notes: Use a safe low-voltage load only*

---

## Wiring Diagram

![Circuit Diagram](../../assets/intermidiate/BLUETOOTH/BLUETOOTH%20SMART%20SWITCH%20PANEL/circuit_1.png)

---

## Step-by-Step Assembly

**Step 1: Place the Raspberry Pi Pico 2W**

Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap.
Keep the USB port facing outward so you can easily connect it to your computer.

**Step 2: Place the Relay Module**

Place the 1-channel relay module beside the breadboard where the control pins are easy to reach.
Identify VCC, GND, IN, IN, COM, NO, and NC before wiring.

**Step 3: Connect Relay VCC**

Connect relay module VCC to the external supply voltage required by the relay module.
Do not power relay coils or external loads from a Pico GPIO pin.

**Step 4: Connect Relay GND**

Connect relay module GND to the external supply GND.
Connect the same GND line to Pico GND unless the relay module is fully opto-isolated and wired for isolation.

**Step 5: Connect IN to GPIO 16**

Connect relay input IN to GPIO 16.

**Step 6: Connect IN to GPIO 17**

Connect relay input IN to GPIO 17.

**Step 7: Wire Load Through Relay**

Connect the external load supply positive wire to Relay COM.
Connect Relay NO to the positive side of Load.
Connect the negative side of Load back to the external supply negative wire.

**Step 8: Wire Load Through Relay**

Connect the external load supply positive wire to Relay COM.
Connect Relay NO to the positive side of Load.
Connect the negative side of Load back to the external supply negative wire.

**Step 9: Check the Load Paths**

Confirm that no load current path passes through the Raspberry Pi Pico 2W.
Use safe low-voltage DC loads only for this student project.

---

**Wiring Check**

- ✓ Pico 2W is placed correctly across the breadboard center gap
- ✓ Relay VCC connects to the correct external relay supply
- ✓ Relay GND connects to external supply GND and Pico GND where required
- ✓ Relay IN1 connects to GPIO 16
- ✓ Relay IN2 connects to GPIO 17
- ✓ Load 1 positive path uses Relay 1 COM and NO
- ✓ Load 2 positive path uses Relay 2 COM and NO
- ✓ No load current is routed through a Pico GPIO pin
- ✓ No loose jumper wires

**Intermediate Note**

This project uses BLE on the Raspberry Pi Pico 2W. Use a BLE app such as nRF Connect, LightBlue, or a BLE UART terminal to connect to `AIDER_SwitchPanel` and send commands. The code treats the relay module as active-low, so a relay may turn on when its input is driven LOW.

**Safety Note**

Use low-voltage DC loads only. Do not wire mains AC in this student project. Use a relay module that can be triggered by a 3.3V GPIO signal, or add a proper driver circuit.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

**Hardware setup**

- Build the relay control side first
- Keep the Pico control wires separate from the load wires so the circuit is easier to debug

**Test the output channels**

- Upload a short relay click test and confirm both channels respond
- If your module is active-low, verify that logic 0 turns a relay on and logic 1 turns it off

**Test the low-voltage loads**

- Use safe LED or lamp loads first
- Switch one relay at a time and confirm the correct load changes state

**Test communication**

- Connect to `AIDER_SwitchPanel` from the BLE app
- Send `status`, `on`, `off`, and `status` while watching the relay channels

**Run the full system**

- Operate the relay channel from the phone
- Confirm that changing Relay does not affect Relay and vice versa
- Use `all off` at the end of the test

**Save the project**

- Save the tested program on the computer
- Label the load wiring if you plan to reuse the panel in the next project

**Additional Testing and Calibration Checks**

- Calibration and tuning notes
- Check whether your relay module is active-low or active-high before trusting the final code
- If the relay behaviour is inverted, test the module with a short script and update `RELAY_ON` and `RELAY_OFF` accordingly
- Label each connected load so you can verify that the correct relay channel switches the correct output

**Quick testing checklist**

- ☐ Relay responds to `on` and `off`
- ☐ Relay responds to `on` and `off`
- ☐ Both loads stay independent
- ☐ `status` reports the correct state
- ☐ `all off` turns both channels off safely

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import Pin
import bluetooth
import time
from ble_uart import BLEUART

DEVICE_NAME = "AIDER_SwitchPanel"
RELAY_ON = 0
RELAY_OFF = 1

relay = Pin(16, Pin.OUT)
ble = bluetooth.BLE()
ble.active(True)
uart = BLEUART(ble, name=DEVICE_NAME)
command_queue = []

def send_line(message):
    print(message)
    uart.write((message + "\n").encode())

def on_rx(data):
    command = data.decode("utf-8").strip().lower()
    if command:
        command_queue.append(command)

def set_relay(turn_on):
    relay.value(RELAY_ON if turn_on else RELAY_OFF)

def relay_text():
    return "ON" if relay.value() == RELAY_ON else "OFF"

uart.on_rx(on_rx)
set_relay(False)
send_line("Bluetooth single-channel switch ready")

while True:
    if command_queue:
        command = command_queue.pop(0)
        if command in ("on", "relay on", "load on"):
            set_relay(True)
            send_line("Relay ON")
        elif command in ("off", "relay off", "load off", "all off"):
            set_relay(False)
            send_line("Relay OFF")
        elif command == "status":
            send_line("Relay:{}".format(relay_text()))
        elif command == "help":
            send_line("Commands: on, off, status, help")
        else:
            send_line("Unknown command. Send help.")
    time.sleep_ms(100)
```

---

## How the Code Works

- **Active-low constants** — Define which logic level turns the relay on and off — *Why It Matters: Many classroom relay modules do not use simple active-high logic*
- **set_relay()** — Wraps the relay control action in one function — *Why It Matters: Keeps both channels consistent and easier to modify*
- **Command parser** — Matches BLE text commands to Relay or Relay actions — *Why It Matters: Lets one phone control multiple outputs clearly*
- **status report** — Returns the state of the relay channel — *Why It Matters: Helps the student confirm the system state after each command*

---

## Expected Result

A connected BLE app can turn the relay on or off independently. Each relay switches only its own low-voltage test load, and the status command reports both channel states clearly.

---

## Troubleshooting

- **Relay clicks but the load stays off** — Possible cause: The load side is wired to the wrong contact — *Solution: Reconnect the external load through COM and NO so the circuit closes when the relay turns on.*
- **Relay state looks reversed** — Possible cause: The module uses the opposite logic level — *Solution: Test the relay with a simple script and update `RELAY_ON` and `RELAY_OFF` to match the actual module.*
- **Pico resets when a relay switches** — Possible cause: Grounding or power wiring is incorrect — *Solution: Separate the load power properly, recheck shared GND wiring, and test with a smaller safe load first.*
- **Phone cannot find the BLE device** — Possible cause: The Pico is not advertising or the BLE helper files are missing — *Solution: Confirm `ble_uart.py` and `ble_advertising.py` are saved on the Pico, restart the board, and scan again from nRF Connect or LightBlue.*
- **Commands do not change the system state** — Possible cause: The phone is connected to the wrong service or the command text is different from the expected command — *Solution: Reconnect to the BLE UART service and send the exact command shown in the test section.*

---

## Challenge Extensions

- **Engineering Challenge:** add a manual local button for each channel so the panel still works when the phone is not connected
- Add a current status LED for each relay output on the control side
- Extend the command set so a timer can turn one channel off automatically after a chosen interval

---

## Reflection Questions

1. Why do relay projects need a different safety mindset from direct LED projects?
2. Why is it important to separate control wiring from load wiring when debugging?
3. What could go wrong if a student tried to connect a mains plug directly to this classroom prototype?
4. How would you redesign this panel for outdoor agricultural equipment?

---

## Save Your Work

Save the file to your computer as:

```
project_103_bluetooth_smart_switch_panel.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

Project 104: Bluetooth Environmental Alarm