# Getting Started

## Introduction

This manual is a guided learning pathway for beginners who want to build real STEM and embedded systems projects using the Raspberry Pi Pico 2 W and MicroPython. It is designed for learners who may be new to programming, electronics, breadboards, sensors, and microcontrollers.

The learning experience is project-based. Learners first understand the board, the programming language, the software tools, safety rules, and wiring basics. After that, they build hands-on projects that gradually introduce digital output, digital input, sensors, buzzers, relays, motors, displays, and connected systems.

| **LEARNING PHILOSOPHY:** Each project should teach one main idea, test each part separately, and then combine the parts into a working system. |
| --- |

## Who This Manual Is For

* Students and young learners beginning electronics and coding.
* Teachers, trainers, and STEM club facilitators.
* Makers who want a structured introduction to MicroPython on the Pico 2 W.
* Learners with little or no previous programming or electronics experience.

## What Learners Will Build

* Simple output circuits such as LEDs and buzzers.
* Input circuits using buttons and sensors.
* Alarm, automation, and control systems.
* Projects that connect code to the physical world.
* Extensions involving motors, relays, displays, and wireless communication.

## Expected Outcomes

* Understand how a microcontroller reads inputs and controls outputs.
* Write and run basic MicroPython programs.
* Use GPIO pins safely with beginner electronics components.
* Read wiring tables and simple circuit diagrams.
* Test and troubleshoot projects step by step.

## How to Use This Manual

**1.** Read the foundational sections before starting the projects.

**2.** Gather all components before wiring the circuit.

**3.** Build slowly and check each connection before applying power.

**4.** Test each component separately before running the full project code.

**5.** Use the troubleshooting tables when something does not work.

**6.** Try challenge extensions only after the base project works.

**7.** Save every finished project with a clear filename.

# 2. About the Raspberry Pi Pico 2 W

The Raspberry Pi Pico 2 W is a small microcontroller board. A microcontroller is like a tiny computer designed to control electronics. It can read sensors, turn devices on and off, produce signals, and communicate with other modules.

| **Feature** | **Beginner-friendly explanation** |
| --- | --- |
| Microcontroller | The main chip that runs your MicroPython program. |
| GPIO pins | Pins that can read inputs or control outputs. |
| USB port | Used for power, programming, and communication with Thonny. |
| 3.3V output | A regulated voltage pin for low-power sensors and modules. |
| GND pins | Ground reference points that complete the circuit. |
| Wireless hardware | Allows Wi-Fi and Bluetooth-based projects when supported by firmware and libraries. |

## GPIO Pins

GPIO means General Purpose Input/Output. A GPIO pin can act like an input or an output depending on how your program configures it.

* **Input:** The pin listens for a signal, such as a button press or sensor output.
* **Output:** The pin sends a signal, such as turning an LED or buzzer on.

| **IMPORTANT:** Pico GPIO pins use 3.3V logic. Do not connect a 5V signal directly to a GPIO pin. |
| --- |

## Digital Input and Output

Digital signals have two main states: LOW and HIGH. LOW is usually close to 0V. HIGH is usually close to 3.3V on the Pico.

## Analog Input

An analog input reads a range of values instead of only ON or OFF. On the Pico 2 W, GPIO26, GPIO27, and GPIO28 are commonly used as exposed ADC inputs.

## PWM

PWM means Pulse Width Modulation. It switches a pin on and off very quickly to create an average output level. PWM is useful for dimming LEDs, servo control signals, and motor speed control with a correct driver.

## Communication Protocols

| **Protocol** | **Use** | **Example** |
| --- | --- | --- |
| UART | Serial communication between devices. | GPS or serial sensor. |
| I2C | Two-wire communication with addressed devices. | OLED display or sensor module. |
| SPI | Fast communication using several wires. | Display or SD card. |
| USB | Programming and serial communication. | Running code from Thonny. |
| Wi-Fi | Wireless networking for connected projects. | Sending sensor data to a dashboard. |

## Power Considerations

* Use the USB cable for beginner projects unless instructed otherwise.
* Use 3V3(OUT) for small 3.3V-safe sensors with low current needs.
* Use external power for motors, relays, servos, pumps, or high-current devices.
* Connect grounds together when using an external supply with Pico signal pins.
* Never power a motor or large buzzer directly from a GPIO pin.