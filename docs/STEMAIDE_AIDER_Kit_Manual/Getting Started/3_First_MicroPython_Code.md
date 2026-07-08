# 3. Introduction to MicroPython

MicroPython is a version of Python designed to run on small microcontroller boards. It lets beginners write readable code while controlling real electronic components.

## What Is MicroPython?

MicroPython is a compact implementation of Python 3 for embedded hardware. It includes useful modules for controlling pins, reading sensors, creating delays, and communicating with devices.

## Why Use MicroPython for Embedded Systems?

* It is beginner-friendly and easier to read than many low-level languages.
* It supports quick testing through the Thonny Shell and REPL.
* It connects code directly to pins, sensors, lights, buzzers, and actuators.

## First Program and print()

The first program prints a message in the Shell. This proves that the editor, interpreter, and Pico connection are working.

**Example: Hello World**

| print("Hello World") |
| --- |

**Example: Printing a value**

| temperature = 25 print("Temperature:", temperature) |
| --- |

## Variables and Data Types

A variable is a name that stores a value. You can think of it as a labelled box in memory.

**Example: Variables**

| student_name = "Ama" age = 12 led_pin = 0 print(student_name, age, led_pin) |
| --- |

| **Data type** | **Example** | **Meaning** |
| --- | --- | --- |
| String | "Hello" | Text |
| Integer | 10 | Whole number |
| Float | 3.14 | Decimal number |
| Boolean | True or False | A yes/no value |
| List | [1, 2, 3] | A group of values |

## Functions

A function is a reusable block of code. Functions keep project code organized.

**Example: Function**

| def greet():  print("Welcome to STEMAIDE Africa")  greet() |
| --- |

## Loops

A loop repeats code. while loops are common in embedded systems because projects usually keep running until power is removed.

**Example: while loop**

| while True:  print("Running...")  time.sleep(1) |
| --- |

**Example: for loop**

| for count in range(5):  print("Count:", count) |
| --- |

## Conditional Statements

**Example: if, elif, else**

| motion_detected = True  if motion_detected:  print("Alarm on") elif False:  print("Other condition") else:  print("No motion") |
| --- |

## Importing Libraries and Delays

Libraries are ready-made code. machine controls hardware, and time creates delays.

**Example: GPIO and time.sleep()**

| from machine import Pin import time  led = Pin(0, Pin.OUT) led.on() time.sleep(1) led.off() |
| --- |

## Common Beginner Mistakes

| **Mistake** | **Why it causes problems** | **Fix** |
| --- | --- | --- |
| Wrong indentation | Python uses indentation to group code. | Use four spaces inside loops, functions, and if statements. |
| Forgetting imports | MicroPython does not know where Pin or time comes from. | Add from machine import Pin and import time. |
| Using physical pin numbers as GPIO numbers | MicroPython code uses GPIO numbers. | Check the wiring table carefully. |
| Saving only to the Pico | A file may be overwritten or lost. | Save a backup on the computer first. |
| Using 5V input on GPIO | This may damage the board. | Use 3.3V-safe signals or a level shifter. |

## Mini Glossary of Programming Terms

| **Term** | **Meaning** |
| --- | --- |
| Program | A set of instructions the Pico runs. |
| Statement | One instruction in a program. |
| Variable | A named place to store a value. |
| Function | A reusable block of code. |
| Loop | Code that repeats. |
| Condition | A test that decides what happens next. |
| Library | Reusable code. |
| Debugging | Finding and fixing errors. |

## Useful Learning Resources

* [MicroPython documentation](https://docs.micropython.org/)
* [MicroPython on Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
* [Python tutorial](https://docs.python.org/3/tutorial/)
* [Raspberry Pi Pico documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [Thonny IDE](https://thonny.org/)