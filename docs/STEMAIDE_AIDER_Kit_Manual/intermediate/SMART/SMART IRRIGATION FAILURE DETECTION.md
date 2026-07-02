# Project 165
## SMART IRRIGATION FAILURE DETECTION

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

This project builds an irrigation monitor that checks whether water is actually flowing during a pump run.

Students will connect a soil moisture sensor, a relay output, and alert devices, then compare measured pulse counts against an expected minimum flow threshold.

The final system should start a short irrigation test, confirm flow in timed windows, and trigger an alert if the system appears to be running without enough water movement.

### Project Story

The real-world use case is a farm or garden irrigation line where a pump may turn on but the pipe could still be blocked, empty, or disconnected.

---

## Learning Objectives

- Use a soil moisture sensor to verify irrigation performance
- Count digital pulses with an interrupt handler
- Compare real sensor data against an expected threshold
- Trigger a relay and an alert output safely
- Test irrigation logic in stages before connecting real water hardware
- Think about how a farm system can fail even when the controller itself seems to be running

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board | Use MicroPython firmware |
| Soil moisture sensor | 1 | Measures water movement during irrigation | Use a 3.3V-compatible pulse output or a level shifter |
| Push button | 1 | Starts the irrigation test cycle | Use with Pico internal pull-up |
| 1-channel relay module | 1 | Switches the pump or valve control line | Use suitable isolation and external power |
| LED and 220 Ω resistor | 1 each | Visual status / alert indicator | Use current limiting |
| Active buzzer | 1 | Audible failure alert | Drive safely from the Pico or use a driver stage |
| External pump power supply | 1 | Powers the real pump or valve | Do not power the pump from the Pico GPIO pins |
| Breadboard and jumper wires | 1 set | Prototype wiring | Disconnect power before rewiring |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules
- Run `import os` and `print(os.listdir())` in the Shell to verify the Pico is connected before saving the project code

### Project-Specific Safety Note

Do not power motors, pumps, or relays directly from the Pico GPIO pins.

Use an external power supply for pumps and motors.

If the relay module is controlled by the Pico, make sure the Pico GND and external power supply GND are connected together unless the relay module is fully opto-isolated and wired correctly.

Keep electronics away from water.

Run flow tests with short safe durations first, and never let a pump dry-run for long during troubleshooting.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Soil moisture sensor signal | GPIO 4 | GPIO 4 / physical pin 6 | Pulse input for interrupt counting |
| Soil moisture sensor VCC | 3.3V or safe interface supply | Module dependent | Follow the sensor datasheet carefully |
| Soil moisture sensor GND | GND | Any GND pin | Common ground |
| Push button one side | GPIO 5 | GPIO 5 / physical pin 7 | Uses internal pull-up |
| Push button other side | GND | Any GND pin | Pressing pulls the input low |
| Relay IN | GPIO 15 | GPIO 15 / physical pin 20 | Pump or valve control output |
| LED anode | GPIO 16 through 220 Ω resistor | GPIO 16 / physical pin 21 | Status or alert indicator |
| LED cathode | GND | Any GND pin | Return path |
| Buzzer positive | GPIO 17 | GPIO 17 / physical pin 22 | Failure alert output |
| Buzzer negative | GND | Any GND pin | Return path |

---

## Wiring Diagram

```
  Raspberry Pi Pico 2 W
  ┌─────────────────────┐
  │                     │
  │  GPIO 4  ───────────┤──── Soil Moisture Sensor Signal
  │  GPIO 5  ───────────┤──── Push Button ──── GND
  │                     │
  │  GPIO 15 ───────────┤──── Relay IN
  │  GPIO 16 ────220Ω───┤──── LED (+)
  │  GPIO 17 ───────────┤──── Buzzer (+)
  │                     │
  │  GND     ───────────┤──── LED (-)
  │  GND     ───────────┤──── Buzzer (-)
  │  GND     ───────────┤──── Soil Sensor GND
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

### Step 2: Place the Flow Sensor
Place the soil moisture sensor in the test water path where it can measure water movement. Identify VCC, GND, and signal output before wiring.

### Step 3: Connect the Flow Sensor
Connect the soil moisture sensor signal wire to GPIO 4. Connect the soil moisture sensor GND to Pico GND. Power the soil moisture sensor only according to its module or datasheet requirements. If the sensor outputs 5V pulses, use a proper level shifter before the Pico input.

### Step 4: Place the Start Button
Place the push button across the breadboard center gap. Connect one side of the button to GPIO 5. Connect the opposite side of the button to GND.

### Step 5: Place and Wire the Relay Module
Identify relay VCC, GND, IN, COM, NO, and NC before wiring. Connect relay IN to GPIO 15. Power the relay module from the supply required by its label. Connect relay GND to Pico GND and to the external pump or valve supply GND where shared grounding is required.

### Step 6: Place and Connect the Status LED
Place the status LED on the breadboard. Identify the long leg as the anode (+) and the short leg as the cathode (-). Connect the status LED long leg through a 220Ω resistor to GPIO 16. Connect the status LED short leg to GND.

### Step 7: Place and Connect the Buzzer
Place the buzzer on the breadboard and identify its positive (+) and negative (-) pins. Connect the buzzer positive pin to GPIO 17. Connect the buzzer negative pin to GND.

### Step 8: Wire the Pump or Valve on the Relay Side
Route the external pump or valve supply positive wire through relay COM and NO. Connect the pump or valve negative lead directly to the external supply negative wire.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Soil moisture sensor signal connects to GPIO 4
- [x] Soil moisture sensor output is confirmed 3.3V-safe before connecting to the Pico
- [x] Start button connects between GPIO 5 and GND
- [x] Relay IN connects to GPIO 15
- [x] Status LED long leg connects through a 220Ω resistor to GPIO 16
- [x] Buzzer positive pin connects to GPIO 17
- [x] Buzzer negative pin connects to GND
- [x] Pump or valve positive path uses relay COM and NO
- [x] No loose jumper wires

> **Intermediate Note**
> Test the soil moisture sensor pulse count before running water through the whole system. The alert depends on pulse count during each test window.

> **Safety Note**
> Keep electronics away from water. Use external power for pumps or valves, confirm soil moisture sensor signal voltage is Pico-safe, and never let a pump run dry.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the button, LED, buzzer, and flow-sensor wiring first with the pump disconnected
- Confirm the soil moisture sensor is mounted in the correct direction if you later use real water flow

### Test the Input Sensor

- Spin or pass water through the soil moisture sensor and confirm the pulse count increases in the Shell
- Press the start button and confirm the Pico detects the request cleanly

### Test the Output Device

- Run a short relay test with no pump connected so you can confirm the relay and LED behaviour safely
- Trigger the failure alert intentionally by setting MIN_PULSES_PER_WINDOW very high and confirm the buzzer works

### Test Communication

- Watch the Shell and verify the program prints the pulse count for each measurement window
- Confirm the printed failure message matches the actual low-flow test condition

### Run the Full System

- Start a test cycle and observe whether each flow window meets the minimum pulse threshold
- If you use a real pump, keep the first tests short and be ready to shut down the water path immediately

### Save the Project

- Save the final code and record the pulse threshold that matched your real flow conditions
- Write down the window length and number of windows used in your final test

### Additional Testing and Calibration Checks

- **Soil moisture sensor test**: generate pulses with water flow or a safe manual sensor test and confirm the count changes
- **Threshold condition test**: choose a realistic minimum pulse count after observing several good-flow runs
- **Output response test**: confirm the relay, LED, and buzzer respond correctly when a failure is triggered
- **Relay click test**: verify the relay turns on only during the test cycle
- **Calibration note**: soil moisture sensors vary, so MIN_PULSES_PER_WINDOW must be tuned using your actual tubing, pump, and water pressure

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, Pin
import time

soil_sensor = ADC(26)
start_button = Pin(5, Pin.IN, Pin.PULL_UP)
relay = Pin(15, Pin.OUT)
status_led = Pin(16, Pin.OUT)
buzzer = Pin(17, Pin.OUT)

RELAY_ON = 1
RELAY_OFF = 0
RUN_SECONDS = 5
SOAK_SECONDS = 8
MIN_MOISTURE_GAIN = 5
SOIL_DRY = 52000
SOIL_WET = 22000

relay.value(RELAY_OFF)
status_led.value(0)
buzzer.value(0)


def clamp(value, low, high):
    return max(low, min(high, value))


def soil_percent():
    raw = soil_sensor.read_u16()
    span = SOIL_DRY - SOIL_WET
    if span <= 0:
        return 0
    return clamp(int(((SOIL_DRY - raw) * 100) / span), 0, 100)


def button_pressed():
    return start_button.value() == 0


def wait_for_button_release():
    while button_pressed():
        time.sleep(0.05)


def alert_failure(message):
    relay.value(RELAY_OFF)
    print('FAILURE:', message)
    for _ in range(3):
        status_led.value(1)
        buzzer.value(1)
        time.sleep(0.25)
        status_led.value(0)
        buzzer.value(0)
        time.sleep(0.25)


def run_irrigation_test():
    before = soil_percent()
    relay.value(RELAY_ON)
    status_led.value(1)
    print('Irrigation test started. Soil before: {}%'.format(before))
    time.sleep(RUN_SECONDS)
    relay.value(RELAY_OFF)
    time.sleep(SOAK_SECONDS)
    after = soil_percent()
    gain = after - before
    if gain < MIN_MOISTURE_GAIN:
        alert_failure('soil moisture increased by only {}%'.format(gain))
        return
    status_led.value(0)
    buzzer.value(0)
    print('Irrigation test passed. Soil moisture gain: {}%'.format(gain))


print('=== Smart Irrigation Failure Detection ===')
while True:
    if button_pressed():
        time.sleep_ms(50)
        if button_pressed():
            run_irrigation_test()
            wait_for_button_release()
    print('Ready. Minimum moisture gain: {}%'.format(MIN_MOISTURE_GAIN))
    time.sleep(2)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| Interrupt pulse counter | Counts flow-sensor pulses whenever the signal rises | Interrupts are more reliable than slow polling for pulse-based sensors |
| sample_flow() | Measures pulses inside a fixed time window | The system needs a consistent measurement period for comparison |
| MIN_PULSES_PER_WINDOW | Defines the minimum acceptable flow performance | This threshold is the key calibration value for failure detection |
| run_irrigation_test() | Starts the relay, checks several flow windows, and stops on failure | Students can see how a controller verifies that output action created the expected result |

---

## Expected Result

When the start button is pressed, the relay should turn on and the system should report the pulse count for each monitoring window.

If the pulse count stays above the minimum threshold in every window, the Shell should report that the irrigation flow test passed.

If the pulse count falls below the threshold, the relay should turn off and the LED and buzzer should alert the user to a likely irrigation failure.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The pulse count stays at zero | The soil moisture sensor signal is not wired correctly or the sensor output level is incompatible | Check the signal path to GPIO 4 and use level shifting if the sensor output is 5V |
| The system reports failure even when water is moving | The threshold is too high for your tubing or pump | Measure several known-good runs and lower MIN_PULSES_PER_WINDOW to a realistic value |
| The relay stays on too long | The program did not exit the test cycle because the button release or timing logic was not observed | Watch the Shell output and test with short window counts first |
| The buzzer and LED do not alert on failure | The output wiring is loose or the failure threshold was never reached | Check GPIO 16 and GPIO 17 wiring, then force a failure by setting a very high threshold temporarily |

---

## Challenge Extensions

- Add a reservoir water level sensor so the system can distinguish low water from a blocked pipe
- Add Bluetooth or Wi-Fi status reporting so irrigation failures can be viewed remotely
- Add a retry mode that attempts one second test cycle before declaring a final failure
- Add data logging so different pump and tubing setups can be compared

---

## Reflection Questions

1. Why is it important to verify flow instead of assuming the pump worked because the relay turned on?
2. Why should the minimum pulse threshold be calibrated for the real hardware?
3. What failures could still happen even if the pulse count looks normal?
4. How would you redesign this system for a multi-zone irrigation farm?

---

## Save Your Work

Save the file to your computer as:

```
project_165_smart_irrigation_failure_detection.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 166: Smart Plant Watering Assistant**