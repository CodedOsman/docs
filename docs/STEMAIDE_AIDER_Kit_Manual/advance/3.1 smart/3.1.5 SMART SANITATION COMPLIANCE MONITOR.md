# Project 198
## Smart Sanitation Compliance Monitor

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

The Pico counts facility uses and shows when a cleaning reset is due after a configured usage threshold.

Cleaning schedules are often based on guesswork rather than on actual usage events.

A Pico 2 W prototype with a PIR sensor, reset button, and status LEDs.

Usage counting, reset logic, and a simple compliance state machine.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

Usage-based cleaning or compliance indicators can support more realistic maintenance planning in sanitation spaces than fixed-time schedules alone.

---

## Learning Objectives

- Cycle between multiple system states
- Represent status clearly with LEDs or indicators
- Use debouncing or event logic to keep the interface reliable
- Explain why local status indicators matter in real operations
- Discuss how a simple status tool could scale into a larger system

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board | Use MicroPython firmware |
| PIR motion sensor | 1 | Detects usage events | Allow warm-up time before counting |
| Push button | 1 | Resets the counter after cleaning | Use internal pull-up or pull-down logic |
| Green LED | 1 | Shows service is current | Add a 220 ohm resistor |
| Red LED | 1 | Shows cleaning is due | Add a 220 ohm resistor |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules.

### Project-Specific Safety Note

Public hygiene or compliance outputs in this project are prototype indicators only and should not replace trained human inspection.

This indicator is a prototype support tool only and does not prove that cleaning was completed correctly.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| PIR OUT | GPIO 14 | GPIO 14 / physical pin 19 | Usage event input |
| Reset button | GPIO 15 to GND when pressed | GPIO 15 / physical pin 20 | Cleaning reset input with pull-up |
| Green LED anode | 220 ohm resistor to GPIO 16 | GPIO 16 / physical pin 21 | Current state indicator |
| Red LED anode | 220 ohm resistor to GPIO 17 | GPIO 17 / physical pin 22 | Cleaning due indicator |

---

## Wiring Diagram

```
  PIR OUT                    -> GPIO 14
  Reset button               -> GPIO 15 and GND
  GPIO 16 -> 220 ohm resistor -> green LED anode
  GPIO 17 -> 220 ohm resistor -> red LED anode
  Common GND                 -> PIR, button, and LEDs
```

---

## Step-by-Step Assembly

1. Connect the PIR output to GPIO 14 and allow warm-up time before testing.
2. Connect one side of the push button to GPIO 15 and the other side to ground.
3. Wire the green and red LEDs to GPIO 16 and GPIO 17 through 220 ohm resistors.
4. Confirm the button changes state in a simple test before using it as a service reset.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Test the PIR so one entry event is counted once rather than continuously.
3. **Test the output device**: Test the reset button and both LEDs with a short script before running the full state machine.
4. **Test the decision logic**: Trigger enough visits to cross the service threshold and then reset the system with the button.
5. **Run the full system**: Run the full system and compare the visit count with the active LED state.
6. **Validate the prototype**: Observe whether PIR placement or room movement causes false usage counts.
7. **Save the project**: Save the validated program on the Pico as main.py and keep a copy on the computer for future edits.

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE, copy and paste this code into a new file or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import Pin
import time

PIR_PIN = 14
BUTTON_PIN = 15
GREEN_LED_PIN = 16
RED_LED_PIN = 17
SERVICE_THRESHOLD = 10

pir = Pin(PIR_PIN, Pin.IN, Pin.PULL_DOWN)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
green_led = Pin(GREEN_LED_PIN, Pin.OUT)
red_led = Pin(RED_LED_PIN, Pin.OUT)
usage_count = 0
occupied = False

print('Cleaning compliance monitor ready')

while True:
    motion = pir.value() == 1
    if motion and not occupied:
        usage_count += 1
        occupied = True
    elif not motion:
        occupied = False

    if button.value() == 0:
        usage_count = 0
        print('Service reset recorded')
        time.sleep(0.3)

    due = usage_count >= SERVICE_THRESHOLD
    green_led.value(0 if due else 1)
    red_led.value(1 if due else 0)
    state = 'DUE' if due else 'CURRENT'
    print('Usage:{} State:{}'.format(usage_count, state))
    time.sleep(0.2)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters | What to Modify During Testing |
|--------------|--------------|----------------|------------------------------|
| Edge-based counting | Counts a visit only when motion first begins | This avoids inflated counts from one person standing still or moving inside the space | Check the counter against real observed visits during testing |
| Service reset | Resets the usage count when the button is pressed | The reset simulates a maintenance or cleaning completion event | Make sure the button is debounced enough for reliable resets |
| Status LEDs | Uses green for current and red for due | A clear visual state helps users interpret the system quickly | Confirm the LED colors match the intended policy during testing |

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

- This prototype is useful for local indicator boards and classroom control panels
- Before deployment, labeling, enclosure design, and user training need improvement
- Status tools only work well when users trust the meaning of each state and keep the system updated

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|---------|----------------|----------|
| Counts increase too quickly | The PIR covers too much of the room or is still warming up | Aim it at the entry path and wait for warm-up before starting validation |
| The reset button does nothing | The button wiring or pull-up logic is wrong | Test GPIO 15 input state in a short button script |
| The red LED never turns on | The threshold is too high or counts are not increasing | Lower the service threshold temporarily and confirm the PIR counting works |
| The count resets by itself | The button wiring is unstable | Secure the button connections and confirm the input stays high when untouched |

---

## Challenge Extensions

- Add a local display showing the active state name
- Add event logging for maintenance review
- Add wireless reporting to a dashboard
- Design a wall-mount enclosure with labels for users

---

## Reflection Questions

1. How could users misunderstand the current status state?
2. What would make the interface more reliable in a busy environment?
3. How would you validate that the status tool reflects reality?
4. What would you add before deploying the system publicly?

---

## Save Your Work

Save the file to your computer as:

```
project_198_smart_sanitation_compliance_monitor.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 199: Environmental Hazard Alert System**