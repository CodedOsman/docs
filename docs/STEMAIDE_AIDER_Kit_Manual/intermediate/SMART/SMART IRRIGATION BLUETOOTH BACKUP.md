# Project 168
## SMART IRRIGATION BLUETOOTH BACKUP

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

This project builds an irrigation controller that can water automatically from soil readings but also accepts manual backup commands over BLE.

Students will combine soil sensing, relay control, cooldown logic, and BLE UART communication into one hybrid control system.

The final system should advertise over BLE, respond to commands such as STATUS, AUTO, ON, OFF, and WATER, and run automatic watering only when the soil is dry and the cooldown period has passed.

### Project Story

The real-world use case is a small irrigation system where automatic soil control is useful, but an operator may still need to force watering or stop the relay from a phone during testing or sensor failure.

---

## Learning Objectives

- Use BLE UART communication on the Pico 2 W
- Standardise BLE helper library naming and setup
- Mix automatic threshold logic with manual backup control
- Use a cooldown timer to prevent rapid repeated watering
- Avoid confusion between BLE app connections and normal Bluetooth pairing
- Test communication and relay outputs separately before full automation

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board with BLE support | Use MicroPython firmware |
| Soil moisture sensor (analog output) | 1 | Measures irrigation need | Keep the sensor electronics dry |
| Relay module or transistor relay driver | 1 | Controls the pump or valve line; some relay boards are active-high while others are active-low | Must suit the load and use external power |
| Status LED and 220 Ω resistor | 1 each | Shows when the relay output is active | Use current limiting |
| External pump or valve power supply | 1 | Powers the real irrigation load | Do not power the load from the Pico GPIO pins |
| Breadboard and jumper wires | 1 set | Prototype wiring | Disconnect power before rewiring |
| Phone with BLE app | 1 | Sends BLE UART commands | Use nRF Connect, LightBlue, or a BLE UART terminal app |

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
- Run `import os` and `print(os.listdir())` in the Thonny Shell and confirm both BLE helper files are visible on the Pico
- **Communication Setup**: install a BLE app such as nRF Connect, LightBlue, or another BLE UART terminal app on your phone
- Scan for the device name `AIDER_IrrigationBackup` after the Pico starts advertising
- Do not pair from the normal phone Bluetooth settings menu. Open the BLE app, scan, connect to the UART-style service, then send text commands from inside the app
- If BLE does not work, restart the Pico and rescan from the BLE app before changing the wiring

### Project-Specific Safety Note

Do not power motors, pumps, or relays directly from the Pico GPIO pins.

Use an external power supply for pumps and valves.

If the relay module is controlled by the Pico, make sure the Pico GND and external power supply GND are connected together unless the relay module is fully opto-isolated and wired correctly.

Keep electronics away from water.

Do not use continuous manual ON mode for long periods during dry-run testing.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Soil sensor VCC | 3.3V | Physical pin 36 | Sensor power |
| Soil sensor GND | GND | Any GND pin | Common ground |
| Soil sensor AOUT | GPIO 26 | GPIO 26 / physical pin 31 | Analog soil input |
| Relay IN | GPIO 15 | GPIO 15 / physical pin 20 | Irrigation relay control; match active-high or active-low behaviour in code |
| Relay VCC and GND | Module dependent | Module dependent | Follow the relay board label carefully |
| Status LED anode | GPIO 16 through 220 Ω resistor | GPIO 16 / physical pin 21 | Output-active indicator |
| Status LED cathode | GND | Any GND pin | Return path |

---

## Wiring Diagram

```
  Raspberry Pi Pico 2 W
  ┌─────────────────────┐
  │                     │
  │  GPIO 26 ───────────┤──── Soil Sensor AOUT
  │                     │
  │  GPIO 15 ───────────┤──── Relay IN
  │  GPIO 16 ────220Ω───┤──── Status LED (+)
  │                     │
  │  3.3V    ───────────┤──── Soil Sensor VCC
  │                     │
  │  GND     ───────────┤──── Soil Sensor GND
  │  GND     ───────────┤──── Status LED (-)
  │  GND     ───────────┤──── Relay GND
  │                     │
  └─────────────────────┘

  Relay Module            External Supply
  ┌──────────┐            ┌────────────┐
  │  COM ────┼────────────┤ (+)        │
  │  NO  ────┼──┐         │            │
  └──────────┘  │         └────────────┘
                │              │
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
Connect soil sensor VCC to 3.3V. Connect soil sensor GND to GND. Connect soil sensor AOUT, AO, or Signal to GPIO 26 (ADC0).

### Step 4: Place and Wire the Relay Driver
Identify relay VCC, GND, IN, COM, NO, and NC before wiring. Connect relay IN to GPIO 15. Power the relay driver according to its board label. Connect relay GND to Pico GND and to the external pump or valve supply GND where shared grounding is required.

### Step 5: Place and Connect the Status LED
Place the status LED on the breadboard. Identify the long leg as the anode (+) and the short leg as the cathode (-). Connect the status LED long leg through a 220Ω resistor to GPIO 16. Connect the status LED short leg to GND.

### Step 6: Wire the Pump or Valve on the Relay Side
Keep the pump or valve power path on the relay contact side, not on the Pico side. Route the external pump or valve supply positive wire through relay COM and NO. Connect the pump or valve negative lead to the external supply negative wire.

### Step 7: Load the BLE Helper Files
Upload `ble_uart.py` and `ble_advertising.py` to the Pico root folder before running the main code. Use `os.listdir()` in the Thonny Shell to confirm both helper files are on the Pico.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Soil sensor AOUT / AO / Signal connects to GPIO 26
- [x] Relay IN connects to GPIO 15
- [x] Relay driver uses external power and shared ground where required
- [x] Status LED long leg connects through a 220Ω resistor to GPIO 16
- [x] Status LED short leg connects to GND
- [x] Pump or valve positive path uses relay COM and NO
- [x] BLE helper files are saved on the Pico
- [x] No loose jumper wires

> **Intermediate Note**
> This project uses BLE on the Raspberry Pi Pico 2W. Use a BLE app such as nRF Connect, LightBlue, or a BLE UART terminal to connect to AIDER_IrrigationBackup. Do not use normal phone Bluetooth pairing. Test STATUS, AUTO, ON, OFF, and WATER commands with the load disconnected first.

> **Safety Note**
> Do not power the pump or valve from the Pico. Use an external supply, keep electronics away from water, and do not use continuous manual ON mode for long dry-run tests.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the soil sensor and relay control wiring first with the real pump disconnected
- Keep the BLE troubleshooting separate from the high-power irrigation side until the relay logic is correct

### Test the Input Sensor

- Read dry and wet soil values so you can tune SOIL_DRY, SOIL_WET, and DRY_THRESHOLD
- Confirm the BLE helper files are present on the Pico before running the final code

### Test the Output Device

- Run a short relay click test with no pump connected and confirm the status LED follows the relay state
- If the relay behaves backward, swap RELAY_ON and RELAY_OFF in the code to match your board before connecting the pump

### Test Communication

- Open the BLE app, scan for AIDER_IrrigationBackup, connect, and send STATUS
- Send ON, OFF, AUTO, and WATER commands and confirm the serial and BLE responses match the relay behaviour

### Run the Full System

- Allow the soil to become dry enough for an automatic watering test and confirm the relay only runs after the cooldown has passed
- Switch between AUTO mode and manual BLE control to verify that backup control works correctly

### Save the Project

- Save the final code and record the BLE device name and command list used in your test
- Write down the dry threshold and cooldown time that matched your irrigation setup

### Additional Testing and Calibration Checks

- **Dry/wet reading test**: record the soil values in dry and wet samples before finalising calibration
- **Device scan test**: confirm the BLE app can find AIDER_IrrigationBackup
- **Connection test**: connect inside the BLE app, not the normal phone Bluetooth settings menu
- **Command test**: send STATUS, AUTO, ON, OFF, and WATER and confirm the reported behaviour matches the relay state
- **Response test**: verify that the Pico sends readable status text back to the phone after each command

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, Pin
import bluetooth
import time
from ble_uart import BLEUART

DEVICE_NAME = 'AIDER_IrrigationBackup'

soil_sensor = ADC(26)
relay = Pin(15, Pin.OUT)
status_led = Pin(16, Pin.OUT)

RELAY_ON = 1
RELAY_OFF = 0
SOIL_DRY = 52000
SOIL_WET = 22000
DRY_THRESHOLD = 35
RECOVERY_THRESHOLD = 50
AUTO_WATER_SECONDS = 4
COOLDOWN_SECONDS = 60
MANUAL_MAX_SECONDS = 20

ble = bluetooth.BLE()
ble.active(True)
uart = BLEUART(ble, name=DEVICE_NAME)

command_queue = []
auto_mode = True
manual_hold = False
manual_started = 0
last_watered = time.time() - COOLDOWN_SECONDS


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def soil_percent():
    raw = soil_sensor.read_u16()
    span = SOIL_DRY - SOIL_WET
    if span <= 0:
        return 0
    percent = int(((SOIL_DRY - raw) * 100) / span)
    return clamp(percent, 0, 100)


def relay_on():
    relay.value(RELAY_ON)
    status_led.value(1)


def relay_off():
    relay.value(RELAY_OFF)
    status_led.value(0)


def send_line(message):
    print(message)
    uart.write((message + '\n').encode())


def on_rx(data):
    command = data.decode('utf-8').strip().upper()
    if command:
        command_queue.append(command)


def stop_manual_hold(reason):
    global manual_hold
    manual_hold = False
    relay_off()
    send_line(reason)


def water_once(reason, seconds):
    global last_watered
    relay_on()
    send_line(reason)
    time.sleep(seconds)
    relay_off()
    last_watered = time.time()


def status_report():
    mode = 'AUTO' if auto_mode else 'MANUAL'
    moisture = soil_percent()
    relay_state = 'ON' if relay.value() == RELAY_ON else 'OFF'
    return 'Mode: {} | Soil: {}% | Relay: {} | Last watered {}s ago'.format(
        mode,
        moisture,
        relay_state,
        int(time.time() - last_watered)
    )


uart.on_rx(on_rx)
relay_off()

print('=== Smart Irrigation Bluetooth Backup ===')
send_line('BLE ready. Use STATUS, AUTO, ON, OFF, or WATER.')

while True:
    now = time.time()
    moisture = soil_percent()

    if manual_hold and (now - manual_started) >= MANUAL_MAX_SECONDS:
        stop_manual_hold('Manual safety timeout reached. Relay turned OFF.')

    if auto_mode and not manual_hold:
        if moisture <= DRY_THRESHOLD and (now - last_watered) >= COOLDOWN_SECONDS:
            water_once('AUTO watering started at {}% soil moisture.'.format(moisture), AUTO_WATER_SECONDS)
        elif moisture >= RECOVERY_THRESHOLD:
            relay_off()

    if command_queue:
        command = command_queue.pop(0)

        if command == 'STATUS':
            send_line(status_report())
        elif command == 'AUTO':
            auto_mode = True
            if manual_hold:
                stop_manual_hold('Returned to AUTO mode. Relay turned OFF.')
            else:
                relay_off()
                send_line('AUTO mode enabled.')
        elif command == 'ON':
            auto_mode = False
            manual_hold = True
            manual_started = time.time()
            relay_on()
            send_line('Manual ON: relay latched. Use OFF to stop.')
        elif command == 'OFF':
            auto_mode = False
            stop_manual_hold('Manual OFF command received. Relay turned OFF.')
        elif command == 'WATER':
            auto_mode = False
            water_once('Manual WATER command started.', AUTO_WATER_SECONDS)
        else:
            send_line('Unknown command. Use STATUS, AUTO, ON, OFF, or WATER.')

    time.sleep(1)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| BLEUART setup | Creates a BLE UART-style service using ble_uart.py and ble_advertising.py | This is the communication layer for phone-based backup control |
| RELAY_ON and RELAY_OFF | Keep the relay drive logic in one place | Students can adapt the code quickly if their relay board is active-low instead of active-high |
| last_watered startup logic | Starts with last_watered set in the past so the system can water immediately if needed | This avoids the common startup mistake of delaying the first valid watering cycle |
| Auto mode logic | Waters automatically only when the soil is dry and the cooldown has expired | This prevents rapid repeated relay activity |
| Manual BLE commands | Allow backup control with STATUS, AUTO, ON, OFF, and WATER commands | Students can test and override the automatic system safely from a phone |

---

## Expected Result

The Pico should advertise as AIDER_IrrigationBackup and respond to BLE UART commands from a BLE app.

In AUTO mode, the relay should run a short watering cycle only when the soil is below the dry threshold and the cooldown has passed.

In MANUAL mode, ON should hold the relay on temporarily, OFF should stop it, WATER should run one short cycle, and STATUS should report the current mode and soil reading.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The phone cannot find the device | The BLE helper files are missing or the Pico did not start advertising | Check that ble_uart.py and ble_advertising.py are on the Pico and restart the board |
| Commands do nothing | The BLE app is not connected to the UART-style service | Open the BLE app, connect to the device, and use the text terminal inside the app instead of normal Bluetooth pairing |
| The relay turns on too often | The cooldown is too short or the dry threshold is too high | Increase COOLDOWN_SECONDS or lower DRY_THRESHOLD after observing real soil readings |
| The relay behaviour is reversed | Your relay board is active-low instead of active-high | Swap RELAY_ON and RELAY_OFF in the code and repeat the relay click test before reconnecting the pump |
| The relay never turns off in manual mode | OFF was not sent or the manual safety timeout has not been reached yet | Send OFF from the BLE app and confirm the command is received in the serial log |

---

## Challenge Extensions

- Design a command set that is still simple for a phone user but prevents unsafe manual watering, such as adding a lockout when the reservoir is empty
- Decide which events should be controlled automatically and which should always require a human confirmation over BLE
- Add a float switch so the system can refuse manual watering when the reservoir is empty
- Add a STATUS response that also reports how many auto watering events happened today
- Add an OLED display that shows BLE connection state and current irrigation mode
- Add a calibration command so dry and wet sensor values can be updated from the phone

---

## Reflection Questions

1. Why is a manual backup useful even when an automatic irrigation system already exists?
2. Why should BLE projects use a BLE app instead of normal Bluetooth pairing settings?
3. Why does a watering system need a cooldown timer?
4. What other safety checks would you add before controlling a real pump outdoors?

---

## Save Your Work

Save the file to your computer as:

```
project_168_smart_irrigation_bluetooth_backup.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 169: Water-Efficient Irrigation Controller**