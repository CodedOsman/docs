# Project 211
## WASTE OVERFLOW ALERT

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

The Pico measures the remaining empty space in a waste bin and raises an alert when the bin is nearly full.

Overflowing bins create sanitation problems when fullness is only noticed after the bin has already become unusable.

A Pico 2 W prototype with an HC-SR04 ultrasonic sensor, LED, and buzzer.

Distance-to-fill logic, alert thresholds, and sensor validation inside a container.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

Bin-fullness monitoring can support smarter waste collection planning, but the prototype must be calibrated for the size and shape of the actual bin.

---

## Learning Objectives

- Read a sensor value or detection signal
- Turn thresholds into clear NORMAL, WARNING, or CRITICAL states
- Coordinate visual and audible alerts
- Check false triggers and calibration limits
- Explain why prototypes are not certified safety systems

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board | Use MicroPython firmware |
| HC-SR04 ultrasonic sensor | 1 | Measures distance to the top of the waste surface | Protect the Echo line for 3.3V-safe use |
| LED | 1 | Bin-full warning LED | Add a 220 ohm resistor |
| Active buzzer | 1 | Critical bin-full alert | Use a low-current buzzer module |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules.
- Measure the empty-bin distance and the almost-full distance before finalizing the alert thresholds.

### Project-Specific Safety Note

Many HC-SR04 ultrasonic modules output 5V on the Echo pin. Raspberry Pi Pico GPIO pins are 3.3V only. Use a voltage divider on the Echo line or use a 3.3V-safe ultrasonic sensor.

Keep the ultrasonic sensor out of contact with trash and mount it firmly at the top of the bin.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| HC-SR04 TRIG | GPIO 14 | GPIO 14 / physical pin 19 | Trigger output |
| HC-SR04 ECHO | GPIO 13 through a voltage divider | GPIO 13 / physical pin 17 | 3.3V-safe echo input |
| LED anode | 220 ohm resistor to GPIO 15 | GPIO 15 / physical pin 20 | Near-full warning LED |
| Buzzer positive | GPIO 16 | GPIO 16 / physical pin 21 | Full alert buzzer |

---

## Wiring Diagram

```
  HC-SR04 TRIG                 -> GPIO 14
  HC-SR04 ECHO                 -> voltage divider -> GPIO 13
  GPIO 15 -> 220 ohm resistor  -> LED anode
  GPIO 16                      -> buzzer positive
  Common GND                   -> ultrasonic sensor, LED, and buzzer
```

---

## Step-by-Step Assembly

1. Mount the ultrasonic sensor at the top of the bin pointing downward.
2. Connect the TRIG line to GPIO 14 and the protected ECHO line to GPIO 13.
3. Wire the LED to GPIO 15 and the buzzer to GPIO 16.
4. Measure the empty-bin and test-fill distances before running the final code.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Validate the sensor at 5 cm, 10 cm, 20 cm, and 30 cm with a flat target before placing it on the bin.
3. **Test the output device**: Test the LED and buzzer outputs independently.
4. **Test the decision logic**: Place filler material inside the bin and confirm the status changes at the chosen thresholds.
5. **Run the full system**: Run the full system and compare the printed distance with the real bin fill level.
6. **Validate the prototype**: Check whether uneven trash surfaces cause false readings or unstable alerts.
7. **Save the project**: Save the validated program on the Pico as main.py and keep a copy on the computer for future edits.

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE, copy and paste this code into a new file or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import Pin
import time

TRIG_PIN = 14
ECHO_PIN = 13
LED_PIN = 15
BUZZER_PIN = 16
WARNING_CM = 18
FULL_CM = 10

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)
buzzer = Pin(BUZZER_PIN, Pin.OUT)

def measure_distance_cm():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    timeout = 30000
    start = time.ticks_us()
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return None
    pulse_start = time.ticks_us()
    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), pulse_start) > timeout:
            return None
    pulse_end = time.ticks_us()
    return (time.ticks_diff(pulse_end, pulse_start) * 0.0343) / 2

print('Waste bin alert ready')

while True:
    distance = measure_distance_cm()
    if distance is None:
        state = 'NO ECHO'
    elif distance <= FULL_CM:
        state = 'FULL'
    elif distance <= WARNING_CM:
        state = 'WARNING'
    else:
        state = 'NORMAL'

    led.value(1 if state in ('WARNING', 'FULL') else 0)
    buzzer.value(1 if state == 'FULL' else 0)
    text_distance = '---' if distance is None else '{:.1f}'.format(distance)
    print('Distance:{}cm State:{}'.format(text_distance, state))
    time.sleep(1)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters | What to Modify During Testing |
|--------------|--------------|----------------|------------------------------|
| Distance measurement | Measures space left between the sensor and the waste surface | This is the evidence the full-bin decision is based on | Record empty and full distances before final tuning |
| Fullness thresholds | Maps distance to NORMAL, WARNING, or FULL | Threshold design determines when the collection team is alerted | Use the actual bin geometry, not guessed values, during calibration |
| Alert outputs | Uses the LED for near-full state and the buzzer for full state | Escalating outputs distinguish between planning and urgent action | Confirm the outputs match the printed state during each test |

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

- This prototype can be used for local warning demonstrations and early field trials
- Before deployment, it needs enclosure protection, calibration records, and a clear response procedure
- Alert systems should always be treated as decision-support tools unless they are certified for the application

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|---------|----------------|----------|
| The bin always looks full | The thresholds are too high or the sensor is mounted too low | Measure the true empty-bin distance and lower the sensor if needed |
| Readings jump around | The trash surface is uneven or the sensor is loose | Mount the sensor securely and test with flatter filler material first |
| No echo is reported | The echo wiring or target angle is wrong | Check the voltage divider and the sensor aim |
| The buzzer never sounds | The full threshold is too strict or the buzzer wiring is wrong | Force a closer target and test the buzzer pin separately |

---

## Challenge Extensions

- Add a second warning level or extra indicator
- Log alert history for later analysis
- Add local display or Wi-Fi communication as a future extension
- Improve the enclosure for harsher environments

---

## Reflection Questions

1. What could cause false alerts in this design?
2. How would you calibrate the thresholds before deployment?
3. What safety risk exists if users trust the prototype too much?
4. How would the system fail in a harsh real environment?

---

## Save Your Work

Save the file to your computer as:

```
project_211_waste_overflow_alert.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 212: Environmental Trend Analyzer**