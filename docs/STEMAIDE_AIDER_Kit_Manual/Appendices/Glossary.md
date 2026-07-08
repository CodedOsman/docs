# 11. Glossary

This project-informed glossary defines beginner terms that appear across the STEMAIDE Africa Raspberry Pi Pico 2 W project set. Learners can use it before, during, and after a project to understand common electronics, programming, sensor, actuator, Wi-Fi, Bluetooth, and IoT language.

## Core Electronics and Pico Terms

| **Term** | **Meaning** |
| --- | --- |
| **3.3V logic** | The safe signal voltage used by Raspberry Pi Pico 2 W GPIO pins. Do not connect 5V signals directly to Pico GPIO pins. |
| **Actuator** | A component that creates action, movement, light, or sound. LEDs, buzzers, relays, motors, and pumps are actuators. |
| **Analog input** | A changing electrical signal that can have many values. Potentiometers, LDR circuits, and some sensors use analog input. |
| **Breadboard** | A reusable board for building circuits without soldering. Rows and power rails connect parts together internally. |
| **Circuit** | A complete path that allows electricity to flow from power, through components, and back to ground. |
| **Common ground** | A shared GND connection between the Pico and other modules or external power supplies. It helps signals have the same reference point. |
| **Current** | The flow of electric charge through a circuit. Too much current can damage components or GPIO pins. |
| **Digital input** | A pin reading that is usually either ON or OFF, HIGH or LOW, 1 or 0. Push buttons and PIR sensor outputs are common examples. |
| **Digital output** | A pin signal controlled by the Pico to turn something on or off, such as an LED, buzzer, or relay input. |
| **GND** | Ground. The zero-volt reference point of the circuit and the return path for current. |
| **GPIO** | General-Purpose Input/Output pin. These are Pico pins that can read sensors or control components. |
| **Jumper wire** | A short wire used to connect the Pico, breadboard, and components. |
| **Logic level** | The voltage range used to represent digital 1 and digital 0. The Pico uses 3.3V logic. |
| **Polarity** | The positive and negative direction of a component. LEDs, buzzers, diodes, and some modules must be connected the correct way. |
| **Resistor** | A component that limits current. It is commonly used to protect LEDs or create sensor input circuits. |
| **Short circuit** | An unsafe direct connection between power and ground or between two points that should not touch. |
| **Signal** | Information carried by a voltage on a wire, such as a button press, sensor reading, or control command. |
| **VCC** | The positive power pin on many modules. Always check whether the module needs 3.3V or 5V. |
| **Voltage** | Electrical pressure that pushes current through a circuit. The Pico uses 3.3V for GPIO signals. |

## Components, Sensors, and Actuators

| **Term** | **Meaning** |
| --- | --- |
| **1N4007 diode** | A protective diode often placed across motors, pumps, or relay coils to reduce voltage spikes when the load turns off. |
| **Active buzzer** | A buzzer that makes sound when powered by a digital output. It does not need a tone signal to produce a simple beep. |
| **BH1750** | A digital light intensity sensor module commonly used to measure brightness in lux. It usually communicates through I2C. |
| **BME280** | A sensor module that can measure temperature, humidity, and air pressure. Many versions communicate through I2C. |
| **DC motor** | A motor that spins when powered by direct current. It usually needs a driver or relay instead of direct GPIO power. |
| **DHT11** | A basic digital humidity and temperature sensor used in beginner environmental monitoring projects. |
| **External power supply** | A separate battery or power adapter used for motors, pumps, relays, or other loads that need more current than the Pico can provide. |
| **IR obstacle sensor** | An infrared sensor that detects nearby objects by sending and receiving infrared light. |
| **IR receiver module** | A module that receives infrared commands from a remote control. |
| **IR remote control** | A handheld remote that sends infrared signals. It can be used to control LEDs, buzzers, or relays. |
| **LDR** | Light-dependent resistor. Its resistance changes with brightness and can be used for light sensing. |
| **LED** | Light-emitting diode. A small light that must be connected with the correct polarity and a current-limiting resistor. |
| **Low-voltage load** | A safe test device such as a small lamp, LED strip, fan, pump, or motor used with a relay or driver. |
| **MAX30102** | A pulse and heart-rate sensor module often used for simple health-monitoring demonstrations. |
| **MOSFET** | An electronic switch used to control higher-current loads such as pumps, motors, or LED strips. |
| **Motor driver** | A module that lets the Pico safely control motors, including speed and direction. |
| **NPN transistor** | A small electronic switch that can let a GPIO pin control a load that needs more current than the GPIO pin can supply. |
| **OLED display** | A small screen used to show text, numbers, sensor readings, menus, or status messages. |
| **PIR motion sensor** | A passive infrared sensor that detects movement from warm objects such as people. |
| **Potentiometer** | A knob-like variable resistor. It can provide an analog input value for brightness or speed control. |
| **Push button** | A simple switch used as a user input. It is often used with a pull-up or pull-down resistor. |
| **Rain sensor module** | A sensor board used to detect water drops or wetness. |
| **Relay module** | An electrically controlled switch. It allows the Pico to control a separate low-voltage load safely when used correctly. |
| **RGB LED** | An LED package with red, green, and blue light channels that can be mixed to create different colors. |
| **SH1106 OLED** | A common OLED display controller used in small I2C display modules. |
| **Soil moisture sensor** | A sensor used to estimate whether soil is wet or dry. |
| **Tachometer sensor** | A sensor used to measure rotation speed, often by counting pulses from a spinning disk or motor shaft. |
| **TCS34725** | A color sensor module that can detect red, green, blue, and clear light levels. |
| **TTP223 touch sensor** | A capacitive touch module that acts like a button when touched. |
| **Water level sensor** | A sensor used to detect or estimate the amount of water in a container. |
| **Water pump** | A small motorized pump used to move water. It should be powered through a driver, MOSFET, or relay rather than directly from GPIO. |

## MicroPython and Programming Terms

| **Term** | **Meaning** |
| --- | --- |
| **ADC** | Analog-to-Digital Converter. It converts an analog voltage into a number the Pico can read. |
| **Boolean** | A value that is either True or False. It is useful for decisions and on/off states. |
| **Condition** | A test in code, usually written with if, elif, or else, that helps the program decide what to do next. |
| **Debouncing** | A technique for ignoring tiny rapid changes from a mechanical button so that one press is counted once. |
| **Duty cycle** | The percentage of time a PWM signal is ON. It is used to control LED brightness or motor speed. |
| **Function** | A named block of code that performs a specific task and can be reused. |
| **Import** | A command that brings a module or library into a program, such as import time or from machine import Pin. |
| **Library** | Reusable code that adds features to a program. Some sensors and displays need library files on the Pico. |
| **Loop** | A part of a program that repeats. while True is commonly used to keep embedded programs running. |
| **MicroPython** | A version of Python designed for microcontrollers such as the Raspberry Pi Pico 2 W. |
| **Module** | A file or package of code that can be imported into a MicroPython program. |
| **Pin object** | A MicroPython object that represents a physical GPIO pin and lets code read or control it. |
| **PWM** | Pulse Width Modulation. A fast ON/OFF signal used to control brightness, sound patterns, or motor speed. |
| **Pull-up resistor** | A resistor or internal setting that keeps an input HIGH until a button or sensor pulls it LOW. |
| **REPL** | Read-Evaluate-Print Loop. An interactive MicroPython prompt where learners can test commands. |
| **Shell** | The area in Thonny where output messages appear and where simple commands can be tested. |
| **time.sleep()** | A MicroPython command that pauses the program for a chosen number of seconds. |
| **Variable** | A named storage place for a value, such as led_state, count, temperature, or threshold. |
| **while True** | A loop that runs forever until the program is stopped or the board loses power. |

## Communication, Wi-Fi, Bluetooth, and IoT Terms

| **Term** | **Meaning** |
| --- | --- |
| **2.4 GHz Wi-Fi** | The Wi-Fi band used by many microcontroller boards. The Pico 2 W connects to 2.4 GHz networks, not 5 GHz-only networks. |
| **BLE** | Bluetooth Low Energy. A low-power form of Bluetooth used for phone-to-device control and sensor displays. |
| **Bluetooth pairing** | The process of connecting a phone or computer to a Bluetooth device so they can communicate. |
| **Cloud display** | A web or online view that shows sensor data or device status from a connected project. |
| **Dashboard** | A simple screen, webpage, or app view that shows project readings and control options. |
| **Data logger** | A project that records values over time, such as temperature, humidity, light level, or button presses. |
| **I2C** | A two-wire communication method often used by sensors and OLED displays. It uses SDA and SCL lines. |
| **IoT** | Internet of Things. A system where physical devices collect data, communicate, or respond through a network. |
| **IP address** | A number that identifies a device on a network. It is often used to open a Pico webpage from a browser. |
| **Local network** | Devices connected to the same Wi-Fi router or access point. |
| **SCL** | The clock line used by I2C devices. It helps coordinate data movement. |
| **SDA** | The data line used by I2C devices. It carries information between the Pico and modules. |
| **SSID** | The name of a Wi-Fi network. |
| **Threshold** | A chosen limit that helps the program decide when to react, such as dry soil, high temperature, or bright light. |
| **UART** | A serial communication method that uses TX and RX pins. It is often used by Bluetooth modules. |
| **Web server** | A program that lets the Pico provide a webpage or respond to browser requests over Wi-Fi. |
| **Wi-Fi station mode** | A mode where the Pico connects to an existing Wi-Fi network as a device on that network. |