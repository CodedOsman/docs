# Project 219
## WATER SAFETY ALARM

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

The Pico reads a turbidity or TDS-style analog input and warns when water quality moves beyond the chosen prototype threshold.

Water quality problems are difficult to notice without a visible or audible alert.

A Pico 2 W prototype with a water-quality proxy sensor, two LEDs, and a buzzer.

Analog thresholding, calibration, and honest interpretation of water-quality proxy data.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

Low-cost water-quality sensors can support classroom discussion about safer water practices, but their readings are proxy measurements and not certified purity results.

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
| Turbidity or TDS analog sensor module | 1 | Provides a water-quality proxy reading | Confirm the analog output is 3.3V safe |
| Green LED | 1 | Shows acceptable prototype range | Add a 220 ohm resistor |
| Red LED | 1 | Shows poor water-quality proxy state | Add a 220 ohm resistor |
| Active buzzer | 1 | Critical alert | Use a low-current buzzer module |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules.
- Treat this sensor as a classroom proxy only. It does not certify safe drinking water.

### Project-Specific Safety Note

Keep electronics away from water and dry the work area before powering the Pico.

Do not immerse the Pico itself, and keep water samples in a stable separate container.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Water-quality sensor AO | GPIO 26 ADC0 | GPIO 26 / physical pin 31 | Analog water-quality proxy input |
| Green LED anode | 220 ohm resistor to GPIO 15 | GPIO 15 / physical pin 20 | Normal-state indicator |
| Red LED anode | 220 ohm resistor to GPIO 16 | GPIO 16 / physical pin 21 | Warning or critical indicator |
| Buzzer positive | GPIO 17 | GPIO 17 / physical pin 22 | Critical alarm |

---

## Wiring Diagram

```
  Sensor AO             -> GPIO 26
  GPIO 15               -> 220 ohm resistor -> green LED anode
  GPIO 16               -> 220 ohm resistor -> red LED anode
  GPIO 17               -> buzzer positive
  Common GND            -> sensor, LEDs, and buzzer
```

---

## Step-by-Step Assembly

1. Connect the analog sensor output to GPIO 26 through a safe ADC path.
2. Wire the green LED to GPIO 15 and the red LED to GPIO 16 through 220 ohm resistors.
3. Connect the buzzer to GPIO 17.
4. Place only the probe or sample interface in the water sample area and keep the Pico dry.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Measure the raw analog value for at least two known sample conditions before setting the thresholds.
3. **Test the output device**: Test the LEDs and buzzer outputs separately.
4. **Test the decision logic**: Switch between clearer and dirtier sample conditions and confirm the system changes state logically.
5. **Run the full system**: Run the full system and compare the printed reading with the output behavior.
6. **Validate the prototype**: Discuss why this proxy measurement is not enough for certified water safety decisions.
7. **Save the project**: Save the validated program on the Pico as main.py and keep a copy on the computer for future edits.

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE, copy and paste this code into a new file or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, Pin
import time

SENSOR_PIN = 26
GREEN_LED_PIN = 15
RED_LED_PIN = 16
BUZZER_PIN = 17
WARNING_LEVEL = 26000
CRITICAL_LEVEL = 42000

sensor = ADC(SENSOR_PIN)
green_led = Pin(GREEN_LED_PIN, Pin.OUT)
red_led = Pin(RED_LED_PIN, Pin.OUT)
buzzer = Pin(BUZZER_PIN, Pin.OUT)

print('Water safety alarm ready')

while True:
    reading = sensor.read_u16()
    if reading >= CRITICAL_LEVEL:
        state = 'CRITICAL'
    elif reading >= WARNING_LEVEL:
        state = 'WARNING'
    else:
        state = 'NORMAL'

    green_led.value(1 if state == 'NORMAL' else 0)
    red_led.value(1 if state in ('WARNING', 'CRITICAL') else 0)
    buzzer.value(1 if state == 'CRITICAL' else 0)
    print('Reading:{} State:{}'.format(reading, state))
    time.sleep(1)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters | What to Modify During Testing |
|--------------|--------------|----------------|------------------------------|
| Analog thresholding | Maps the proxy reading into NORMAL, WARNING, or CRITICAL | Thresholds are the basis of the interpretation in this prototype | Use measured sample values instead of guessing thresholds |
| Staged indicators | Uses LEDs and the buzzer to reflect the chosen state | Layered outputs help distinguish mild and strong warning conditions | Confirm all outputs match the printed state during testing |
| Prototype framing | Keeps the decision local and simple | Honest framing prevents overclaiming sensor capability | Explain clearly that this is not a certified water test |

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
| The red LED is always on | The thresholds are too low or the sensor output is out of range | Measure the clean-sample baseline first and adjust the thresholds |
| The reading never changes | The sensor is not powered or the sample conditions are too similar | Confirm the analog output and compare more distinct sample conditions |
| The buzzer never sounds | The critical threshold is too high or the buzzer wiring is wrong | Force a stronger test condition and test the buzzer pin separately |
| Values seem noisy | The analog wiring is loose or the sample is unstable | Shorten the analog wire and keep the sample conditions steady during testing |

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
project_219_water_safety_alarm.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 220: Environmental Data Comparison**