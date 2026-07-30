# Project 215
## FLOOD EVACUATION ALERT

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

The Pico monitors water height with an ultrasonic sensor and raises a local alert when the level reaches a warning or critical threshold.

Communities often react too late when drains, rivers, or flood channels are already near overflow.

A Pico 2 W prototype with an HC-SR04 ultrasonic sensor, LED, and buzzer.

Water-level thresholding, alert escalation, and calibration of known distances.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

A local alert prototype can support earlier maintenance or evacuation decisions in a flood-prone area or evacuation route if the thresholds are calibrated and validated carefully.

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
| HC-SR04 ultrasonic sensor | 1 | Measures distance to the water surface | Protect the Echo line for 3.3V-safe use |
| LED | 1 | Visual alert output | Add a 220 ohm resistor |
| Active buzzer | 1 | Audible alert output | Use a low-current buzzer module |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules.
- Calibrate the warning distances against the real mounting height.

### Project-Specific Safety Note

Keep electronics away from water and dry the work area before powering the Pico.

Many HC-SR04 ultrasonic modules output 5V on the Echo pin. Raspberry Pi Pico GPIO pins are 3.3V only. Use a voltage divider on the Echo line or use a 3.3V-safe ultrasonic sensor.

Keep the ultrasonic module above splash level and protect the Echo line with a voltage divider if needed.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| HC-SR04 TRIG | GPIO 14 | GPIO 14 / physical pin 19 | Trigger output |
| HC-SR04 ECHO | GPIO 13 through a voltage divider | GPIO 13 / physical pin 17 | 3.3V-safe echo input |
| LED anode | 220 ohm resistor to GPIO 15 | GPIO 15 / physical pin 20 | Visual warning |
| Buzzer positive | GPIO 16 | GPIO 16 / physical pin 21 | Critical alert |

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

1. Connect the ultrasonic TRIG pin to GPIO 14.
2. Connect the ECHO pin to GPIO 13 through a voltage divider or use a 3.3V-safe sensor module.
3. Wire the LED to GPIO 15 through a 220 ohm resistor and connect the buzzer to GPIO 16.
4. Mount the sensor above the water target so a smaller distance means higher water.
5. Keep the Pico itself away from water and splashing during tests.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Validate the sensor at 5 cm, 10 cm, 20 cm, and 30 cm using a flat target.
3. **Test the output device**: Test the LED and buzzer outputs with standalone scripts before integrating the alert logic.
4. **Test the decision logic**: Move the target across the threshold distances and confirm the alert states change correctly.
5. **Run the full system**: Run the full system and compare the printed distances with the output behavior.
6. **Validate the prototype**: Check for false alerts caused by angled targets, splashes, or unstable sensor mounting.
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
WARNING_CM = 20
CRITICAL_CM = 10

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
    pulse = time.ticks_diff(pulse_end, pulse_start)
    return (pulse * 0.0343) / 2

print('Ultrasonic water alert ready')

while True:
    distance = measure_distance_cm()
    if distance is None:
        level = 'NO ECHO'
    elif distance <= CRITICAL_CM:
        level = 'CRITICAL'
    elif distance <= WARNING_CM:
        level = 'WARNING'
    else:
        level = 'NORMAL'

    led.value(1 if level in ('WARNING', 'CRITICAL') else 0)
    buzzer.value(1 if level == 'CRITICAL' else 0)
    text_distance = '---' if distance is None else '{:.1f}'.format(distance)
    print('Distance:{}cm Level:{}'.format(text_distance, level))
    time.sleep(1)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters | What to Modify During Testing |
|--------------|--------------|----------------|------------------------------|
| Ultrasonic measurement | Measures distance to the water surface using echo timing | This is the core sensing method in the alert system | Verify the distance with a ruler during calibration |
| Threshold logic | Maps distance to NORMAL, WARNING, or CRITICAL | Threshold design determines when the user is warned | Adjust the thresholds only after real distance measurements |
| Alert outputs | Uses the LED for warning and the buzzer for critical alerts | Different outputs help users recognize severity quickly | Test the buzzer only after the LED path is working correctly |

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
| No echo is reported | The sensor is out of range or the Echo wiring is wrong | Check the target distance and verify the Echo voltage divider wiring |
| The buzzer stays on | The critical threshold is too high or the measured distance is too small | Measure the actual empty distance and reduce sensitivity if needed |
| The LED never lights | The threshold is not being crossed or the LED wiring is wrong | Use a closer target to force a warning state and test the LED pin separately |
| Distance readings jump around | The sensor is loose or the target is reflecting poorly | Mount the sensor firmly and test against a flatter target surface |

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
project_215_flood_evacuation_alert.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 216: Drainage IoT Dashboard**