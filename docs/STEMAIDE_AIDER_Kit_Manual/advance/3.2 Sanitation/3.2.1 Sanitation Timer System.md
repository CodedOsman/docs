# Project 204
## SANITATION TIMER SYSTEM

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

The Pico detects entry into a sanitation area and starts a timed hygiene or awareness sequence using local indicators.

Users often need clear, repeated reminders to complete basic hygiene steps correctly and consistently.

A Pico 2 W prototype with a PIR sensor, LED, and buzzer.

Timed reminders, occupancy detection, and user-facing state design.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

Awareness systems are useful when they present simple, repeatable reminders, but they still depend on user behavior and cannot prove that hygiene was completed correctly.

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
| PIR motion sensor | 1 | Detects a person entering the area | Allow warm-up time before testing |
| LED | 1 | Shows active reminder state | Add a 220 ohm resistor |
| Active buzzer | 1 | Provides short reminder beeps | Use a low-current buzzer module |

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

This prototype provides reminders only. It does not verify proper handwashing or hygiene quality.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| PIR OUT | GPIO 14 | GPIO 14 / physical pin 19 | Entry detection input |
| LED anode | 220 ohm resistor to GPIO 15 | GPIO 15 / physical pin 20 | Reminder LED |
| Buzzer positive | GPIO 16 | GPIO 16 / physical pin 21 | Timed reminder beep |

---

## Wiring Diagram

```
  PIR OUT                     -> GPIO 14
  GPIO 15 -> 220 ohm resistor -> LED anode
  GPIO 16                     -> buzzer positive
  Common GND                  -> PIR, LED, and buzzer
```

---

## Step-by-Step Assembly

1. Connect the PIR output to GPIO 14 and allow warm-up time before testing.
2. Wire the LED to GPIO 15 through a 220 ohm resistor and connect the buzzer to GPIO 16.
3. Place the PIR so it detects entry into the reminder zone rather than movement across the whole room.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Test the PIR input and confirm a new entry event is detected only once per visit.
3. **Test the output device**: Test the LED and buzzer with a simple blink and beep script.
4. **Test the decision logic**: Trigger the timer and observe whether the countdown phases occur at the expected times.
5. **Run the full system**: Run the full system and compare the printed reminder state with the user-facing outputs.
6. **Validate the prototype**: Check whether people standing nearby trigger false reminders.
7. **Save the project**: Save the validated program on the Pico as main.py and keep a copy on the computer for future edits.

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE, copy and paste this code into a new file or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import Pin
import time

PIR_PIN = 14
LED_PIN = 15
BUZZER_PIN = 16
DURATION_SECONDS = 20

pir = Pin(PIR_PIN, Pin.IN, Pin.PULL_DOWN)
led = Pin(LED_PIN, Pin.OUT)
buzzer = Pin(BUZZER_PIN, Pin.OUT)
sequence_active = False
sequence_start = 0
occupied = False

print('Awareness timer ready')

while True:
    motion = pir.value() == 1
    now = time.time()

    if motion and not occupied:
        occupied = True
        sequence_active = True
        sequence_start = now
        print('Reminder sequence started')
    elif not motion:
        occupied = False

    if sequence_active:
        elapsed = now - sequence_start
        remaining = DURATION_SECONDS - elapsed
        led.value(0 if int(elapsed) % 2 else 1)
        buzzer.value(1 if int(elapsed) in (0, 10, 19) else 0)
        print('Remaining:{}s'.format(max(0, int(remaining))))
        if remaining <= 0:
            sequence_active = False
            led.value(0)
            buzzer.value(0)
            print('Reminder sequence complete')
    else:
        led.value(0)
        buzzer.value(0)

    time.sleep(0.2)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters | What to Modify During Testing |
|--------------|--------------|----------------|------------------------------|
| Entry detection | Starts the reminder sequence only when a new PIR event begins | This prevents the timer from restarting on every loop | Validate the PIR placement so background motion does not retrigger the timer |
| Countdown timing | Keeps the sequence active for a fixed reminder duration | The timing makes the system feel purposeful to the user | Adjust the duration during testing if 20 seconds is not appropriate |
| Timed outputs | Flashes the LED and beeps the buzzer at defined moments | Different timed cues make the reminder easier to notice | Reduce buzzer usage if the classroom environment becomes too noisy |

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
| The timer restarts constantly | The PIR is retriggering too often or the placement is poor | Aim it at the entry path and reduce extra motion in the background |
| The LED never flashes | The sequence is not starting or the LED wiring is wrong | Print the PIR state first and test GPIO 15 with a simple blink script |
| The buzzer is always on | The timing condition is wrong or the buzzer wiring is reversed | Check the timed beep logic and test the buzzer separately |
| Nothing happens when someone enters | The PIR is not powered or has not warmed up | Wait for warm-up and confirm the output state on GPIO 14 |

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
project_204_sanitation_timer_system.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 205: Environmental Sensor Network**