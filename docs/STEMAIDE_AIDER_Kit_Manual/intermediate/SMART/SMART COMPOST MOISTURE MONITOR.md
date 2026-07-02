# Project 160
## SMART COMPOST MOISTURE MONITOR

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

This project monitors compost moisture and interprets the reading using a moisture range that supports healthy decomposition.

Students will calibrate a moisture sensor, define a compost target range, and use repeated confirmations before calling the compost too dry or too wet.

The final system should report whether the compost is optimal, drying out, or becoming too wet, and it should suggest what action to take.

### Project Story

The real-world use case is a compost bin or organic-waste trial where the pile should stay moist enough for microbial activity but not so wet that airflow is lost.

---

## Learning Objectives

- Adapt a generic soil sensor to a compost-management problem
- Use a range-based target instead of one threshold only
- Require repeated out-of-range readings before declaring a strong alert
- Translate a sensor state into a practical maintenance action
- Think about how compost moisture management differs from normal plant irrigation

---

## Required Components

| Component Name | Quantity | Short Description | Important Note |
|----------------|----------|-------------------|----------------|
| Raspberry Pi Pico 2 W | 1 | Main controller | Use MicroPython |
| Moisture sensor | 1 | Compost moisture input | Calibrate before final testing |
| Green LED and 220 Ω resistor | 1 each | Optimal-state indicator | Current-limited output only |
| Red LED and 220 Ω resistor | 1 each | Confirmed dry or wet alert | Current-limited output only |
| Breadboard and jumper wires | 1 set | Prototype wiring | Keep the sensor wiring stable |

---

## Before You Begin

Before starting this project, make sure you have completed the foundational sections at the beginning of the manual:

- **Software Installation and Setup**
- **Safety Guidelines**
- **Breadboard Basics**
- **Reading Circuit Diagrams**

### Project-Specific Setup Notes

- No external library is required. This project uses only built-in MicroPython modules

### Project-Specific Safety Note

Compost can be wet, dirty, and corrosive, so keep the Pico and USB cable away from the pile.

Clean the sensor after compost testing so residue does not affect later projects.

---

## Circuit Connections

| Component Pin | Connects To | Pico GPIO / Physical Pin Number | Notes |
|---------------|-------------|---------------------------------|-------|
| Moisture sensor VCC | 3.3V | Physical pin 36 | Sensor power |
| Moisture sensor GND | GND | Physical pin 38 | Common ground |
| Moisture sensor AOUT | GPIO 26 | GPIO 26 / physical pin 31 | ADC moisture input |
| Green LED anode | GPIO 16 through 220 Ω resistor | GPIO 16 / physical pin 21 | Optimal-state indicator |
| Red LED anode | GPIO 17 through 220 Ω resistor | GPIO 17 / physical pin 22 | Confirmed dry/wet alert |
| Both LED cathodes | GND | Any GND pin | Common return |

---

## Wiring Diagram

```
  Raspberry Pi Pico 2 W
  ┌─────────────────────┐
  │                     │
  │  GPIO 26 ───────────┤──── Moisture Sensor AOUT
  │                     │
  │  GPIO 16 ────220Ω───┤──── Green LED (+)
  │  GPIO 17 ────220Ω───┤──── Red LED (+)
  │                     │
  │  3.3V    ───────────┤──── Moisture Sensor VCC
  │                     │
  │  GND     ───────────┤──── Moisture Sensor GND
  │  GND     ───────────┤──── Green LED (-)
  │  GND     ───────────┤──── Red LED (-)
  │                     │
  └─────────────────────┘
```

---

## Step-by-Step Assembly

### Step 1: Place the Raspberry Pi Pico 2W
Place the Raspberry Pi Pico 2W on the breadboard so it sits across the center gap. Keep the USB port facing outward so you can easily connect it to your computer.

### Step 2: Position the Compost Moisture Sensor
Place the moisture probe so only the sensing end enters the compost sample area. Identify VCC, GND, and AOUT / AO / Signal on the sensor module.

### Step 3: Connect the Moisture Sensor
Connect moisture sensor VCC to **3.3V**. Connect moisture sensor GND to **GND**. Connect moisture sensor AOUT, AO, or Signal to **GPIO 26** (ADC0).

### Step 4: Place and Connect the Green LED
Place the green LED on the breadboard. Identify the long leg as the anode (+) and the short leg as the cathode (-). Connect the green LED long leg through a 220Ω resistor to **GPIO 16**. Connect the green LED short leg to **GND**.

### Step 5: Place and Connect the Red LED
Place the red LED on the breadboard. Identify the long leg as the anode (+) and the short leg as the cathode (-). Connect the red LED long leg through a 220Ω resistor to **GPIO 17**. Connect the red LED short leg to **GND**.

### Step 6: Keep the Compost Area Separate
Keep the Pico, breadboard, USB cable, and jumper wires away from the compost sample. Clean the sensor after compost testing so residue does not affect later projects.

### Wiring Check

- [x] Pico 2W is placed correctly across the breadboard center gap
- [x] Moisture sensor VCC connects to 3.3V
- [x] Moisture sensor GND connects to GND
- [x] Moisture sensor AOUT / AO / Signal connects to GPIO 26
- [x] Green LED long leg connects through a 220Ω resistor to GPIO 16
- [x] Red LED long leg connects through a 220Ω resistor to GPIO 17
- [x] Both LED short legs connect to GND
- [x] No loose jumper wires

> **Intermediate Note**
> Test a dry sample and a damp sample before judging the compost state. Compost readings are a learning proxy, so watch for stable trends rather than one perfect number.

> **Safety Note**
> Compost can be wet, dirty, and corrosive. Keep the Pico and USB cable away from the sample, and clean the sensor after testing.

---

## Testing Individual Components

Before running the full project, test each part separately. This makes it easier to find wiring, library, or code problems.

### Hardware Setup

- Build the moisture sensor and LED wiring before inserting the sensor into compost
- Prepare a small test sample first instead of the full compost bin

### Test the Input Sensor

- Calibrate the sensor with drier and wetter compost-like material or controlled test media
- Observe how the moisture percentage changes when water is added or dry material is mixed in

### Test the Output Devices

- Test both LEDs before relying on the compost-state logic
- Confirm that the red LED only comes on after repeated dry or wet confirmations

### Run the Full System

- Leave the sensor in the compost sample and observe how the state changes over several readings
- Compare the printed advice with the actual texture of the compost material

### Save the Project

- Save the final code and record the compost moisture range used in your test
- Write down whether the confirmation counter reduced false alerts effectively

### Additional Testing and Calibration Checks

**Calibration and tuning notes**

- Calibrate the sensor using material that behaves like your compost sample, not only plain water or dry air
- Use the repeated-confirmation logic to avoid acting on a single noisy reading
- If the compost dries or wets very slowly, be patient and observe several readings before changing the thresholds
- Clean the probe after testing because compost residue can affect later measurements

**Quick testing checklist**

- [ ] Moisture percentage changes when the compost sample changes
- [ ] Green LED shows the optimal range
- [ ] Red LED shows confirmed dry or wet problems
- [ ] The Shell prints action advice, not only a raw number
- [ ] Repeated confirmations reduce false alerts

---

## Full Project Code

After completing and checking the circuit connections, open Thonny IDE. Copy and paste the code below into a new file, or upload the project file to the Raspberry Pi Pico 2 W, then run it from Thonny.

```python
from machine import ADC, Pin
import time

soil = ADC(26)
green_led = Pin(16, Pin.OUT)
red_led = Pin(17, Pin.OUT)

soil_dry = 52000
soil_wet = 22000
optimal_min = 50
optimal_max = 70
confirm_count = 3
dry_hits = 0
wet_hits = 0


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def moisture_percent():
    raw = soil.read_u16()
    span = soil_dry - soil_wet
    if span == 0:
        return 0
    percent = int(((soil_dry - raw) * 100) / span)
    return clamp(percent, 0, 100)


def compost_state(moisture):
    global dry_hits, wet_hits

    if optimal_min <= moisture <= optimal_max:
        dry_hits = 0
        wet_hits = 0
        return "OPTIMAL", "Maintain current moisture and turn the pile as needed"

    if moisture < optimal_min:
        dry_hits += 1
        wet_hits = 0
        if dry_hits >= confirm_count:
            return "TOO DRY", "Add water gradually and mix the compost"
        return "WATCH DRY", "Dry trend not yet confirmed"

    wet_hits += 1
    dry_hits = 0
    if wet_hits >= confirm_count:
        return "TOO WET", "Add dry brown material and improve aeration"
    return "WATCH WET", "Wet trend not yet confirmed"


print("Smart compost moisture monitor ready")

while True:
    moisture = moisture_percent()
    state, advice = compost_state(moisture)

    green_led.value(1 if state == "OPTIMAL" else 0)
    red_led.value(1 if state in ("TOO DRY", "TOO WET") else 0)

    print("Moisture:{}% State:{} Advice:{}".format(moisture, state, advice))

    time.sleep(5)
```

---

## How the Code Works

| Code Section | What It Does | Why It Matters |
|--------------|--------------|----------------|
| `optimal_min` and `optimal_max` | Define the compost target range | Compost moisture has a useful range, not only a dry threshold |
| `confirm_count` | Requires repeated out-of-range readings before a strong alert is declared | One noisy reading should not force unnecessary compost changes |
| `compost_state()` | Maps moisture readings to OPTIMAL, WATCH, TOO DRY, or TOO WET states | Advice should match the actual compost-management action |
| LED logic | Shows optimal versus confirmed problem states | Students can quickly check whether the compost needs action |

---

## Expected Result

When the compost moisture stays inside the target range, the green LED should stay on and the Shell should report OPTIMAL. If the pile remains too dry or too wet for several consecutive readings, the red LED should turn on and the Shell should suggest whether to add water, dry material, or more aeration.

---

## Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| The compost is always marked dry | Calibration is wrong or the sample is not contacting the sensor well | Recalibrate the sensor and ensure the probe is inserted properly |
| The red LED never turns on | The confirmation counter is too high or the sample never stays out of range long enough | Reduce `confirm_count` slightly for testing and verify the moisture range |
| The advice seems wrong | The optimal range does not match your compost material | Tune `optimal_min` and `optimal_max` after observing real compost behaviour |
| The readings become unstable after testing | Compost residue remains on the sensor | Clean and dry the sensor before the next run |

---

## Challenge Extensions

- Add temperature sensing to study compost heat and moisture together
- Log compost moisture over several days to compare wetting and drying behaviour
- Add a small reminder output that prompts the user to turn the pile when moisture trends poorly

---

## Reflection Questions

1. Why does compost management need a moisture range instead of just one threshold?
2. Why can a single noisy reading be misleading in compost monitoring?
3. How is compost moisture management different from watering a plant?
4. What other measurements would make this compost monitor more useful?

---

## Save Your Work

Save the file to your computer as:

```
project_160_smart_compost_moisture_monitor.py
```

If you want the program to run automatically when the Pico powers on, save the final version to the Pico as:

```
main.py
```

---

## Next Project

**Project 161: Smart Plant Disease Indicator**