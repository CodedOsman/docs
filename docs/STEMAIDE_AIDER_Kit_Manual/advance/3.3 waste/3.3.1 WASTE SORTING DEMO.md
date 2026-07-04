# Project 203
## WASTE SORTING DEMO

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

The Pico classifies a detected item as dry or wet using a moisture-style sensor and moves a servo to the matching bin position.

Waste sorting is difficult for learners to understand without a visible mechanism that links sensor data to a sorting action.

A Pico 2 W prototype with an IR detection sensor, moisture sensor, servo, and status LED.

Item detection, rule-based sorting, and safe servo actuation.

### Project Story

**Advanced Project**: This advanced project is designed to help learners move beyond basic wiring and coding into complete system thinking. The learner should build the prototype, test each subsystem, validate the data, explain the design decisions, and propose improvements for real-world deployment.

Automated waste sorting prototypes help learners discuss decision logic and mechanical output, even when the final classroom model uses only a simplified dry-versus-wet rule.

---

## Learning Objectives

- Read a sensor or command input and control a relay-driven load
- Use thresholds, hysteresis, or timing to avoid unstable switching
- Test the relay path safely before attaching the real load
- Validate actuator behavior against the decision logic
- Explain power, safety, and deployment limitations

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller board | Use MicroPython firmware |
| IR obstacle sensor | 1 | Detects when an item is presented for sorting | Check whether the output is active low |
| Moisture sensor module | 1 | Provides a dry-versus-wet proxy input | Protect the ADC if required |
| Servo motor | 1 | Moves the sorting gate | Power the servo from an external 5V supply |
| LED | 1 | Shows that a sort decision happened | Add a 220 ohm resistor |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules.
- The servo is driven with PWM in MicroPython.

### Project-Specific Safety Note

Use an external power supply for pumps, fans, and other inductive loads.

Power the servo from an external 5V supply and connect the external ground to the Pico ground before testing.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| IR sensor OUT | GPIO 14 | GPIO 14 / physical pin 19 | Item detection input |
| Moisture sensor AO | GPIO 26 ADC0 | GPIO 26 / physical pin 31 | Dry-versus-wet proxy input |
| Servo signal | GPIO 15 | GPIO 15 / physical pin 20 | PWM servo control |
| LED anode | 220 ohm resistor to GPIO 16 | GPIO 16 / physical pin 21 | Sort event indicator |

---

## Wiring Diagram

```
  IR sensor OUT               -> GPIO 14
  Moisture sensor AO          -> GPIO 26
  Servo signal                -> GPIO 15
  GPIO 16 -> 220 ohm resistor -> LED anode
  External 5V                 -> servo power
  Common GND                  -> Pico GND and servo GND
```

---

## Step-by-Step Assembly

1. Connect the IR sensor output to GPIO 14.
2. Connect the moisture sensor analog output to GPIO 26 through a safe ADC path.
3. Connect the servo signal wire to GPIO 15 and power the servo from an external 5V supply.
4. Tie the servo supply ground to the Pico ground so the PWM signal has a common reference.
5. Wire the LED to GPIO 16 through a 220 ohm resistor.

---

## Testing Individual Components

Before running the full project, test each subsystem separately. This makes it easier to find wiring, library, or logic problems before full integration.

1. **Hardware setup**: Assemble the Pico, sensor, indicator, and load wiring exactly as shown in the connection table before applying power.
2. **Test the input sensor**: Test the IR sensor and moisture sensor separately before moving the servo.
3. **Test the output device**: Test the servo by moving it to left, center, and right positions with a short PWM script.
4. **Test the decision logic**: Present dry and wet samples and confirm the servo chooses the correct side.
5. **Run the full system**: Run the full sorter and compare the printed category with the actual mechanical movement.
6. **Validate the prototype**: Discuss which materials would confuse a dry-versus-wet rule in real waste sorting.
7. **Save the project**: Save the validated program on the Pico as main.py and keep a copy on the computer for future edits.

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE, copy and paste this code into a new file or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, PWM, Pin
import time

IR_PIN = 14
MOISTURE_PIN = 26
SERVO_PIN = 15
LED_PIN = 16
ACTIVE_STATE = 0
WET_THRESHOLD = 30000

ir_sensor = Pin(IR_PIN, Pin.IN, Pin.PULL_UP)
moisture_sensor = ADC(MOISTURE_PIN)
servo = PWM(Pin(SERVO_PIN))
servo.freq(50)
led = Pin(LED_PIN, Pin.OUT)
ready_for_next = True

def set_servo_us(pulse_us):
    duty = int(pulse_us * 65535 / 20000)
    servo.duty_u16(duty)

print('Waste sorting demo ready')
set_servo_us(1500)

while True:
    detected = ir_sensor.value() == ACTIVE_STATE
    if detected and ready_for_next:
        ready_for_next = False
        reading = moisture_sensor.read_u16()
        if reading >= WET_THRESHOLD:
            label = 'WET'
            set_servo_us(2000)
        else:
            label = 'DRY'
            set_servo_us(1000)
        led.value(1)
        print('Moisture:{} Sort:{}'.format(reading, label))
        time.sleep(1)
        set_servo_us(1500)
        led.value(0)
    elif not detected:
        ready_for_next = True

    time.sleep(0.1)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters | What to Modify During Testing |
|--------------|--------------|----------------|------------------------------|
| Item detection | Starts a sort only when a new item is present | This prevents repeated sorting actions on the same item | Check the sensor active state if sorting never starts |
| Threshold classification | Uses one moisture threshold to choose DRY or WET | The sorter must explain clearly why the gate moved | Test several sample materials before finalizing the threshold |
| Servo movement | Moves the gate to the selected side and then returns to center | A predictable servo pattern makes the demo easier to observe and debug | Always test the servo with external power and shared ground first |

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

- This prototype could be used in school, farm, or sanitation demonstrations with safe low-voltage loads
- Before deployment, the load wiring, enclosure, and power design need careful review
- Actuator systems need maintenance planning because relay wear and sensor drift affect reliability

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|---------|----------------|----------|
| The servo jitters | The servo power is unstable or the ground is not shared | Use a stronger external 5V supply and connect the grounds together |
| Every item goes to one side | The threshold is poorly chosen or the moisture readings are not changing | Measure dry and wet sample values first and then adjust the threshold |
| Sorting triggers repeatedly | The IR sensor remains active and the logic is retriggering | Make sure the item leaves the detection zone fully before the next test |
| The LED flashes but the servo does not move | The PWM or servo power wiring is wrong | Test the servo alone with center and end positions first |

---

## Challenge Extensions

- Add a manual override button or maintenance mode
- Add data logging so switching behavior can be reviewed later
- Add a second sensor to confirm decisions before driving the load
- Design a safer enclosure and wiring harness for field testing

---

## Reflection Questions

1. What failure mode could switch the load at the wrong time?
2. How would you make the relay decision more reliable in the field?
3. What safety risk is introduced when controlling a real actuator?
4. What sensor or control change would improve deployment readiness?

---

## Save Your Work

Save the file to your computer as:

```
project_203_waste_sorting_demo.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 204: Sanitation Timer System**