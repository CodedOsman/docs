# 4. Software Installation and Setup

This section centralizes setup instructions. Do not repeat this full setup inside every project. Individual projects should only mention special software or library needs.

## Installing Thonny IDE

**1.** Open https://thonny.org/.

**2.** Download the installer for your operating system.

**3.** Install Thonny using the default options.

**4.** Open Thonny after installation.

## Connecting the Pico 2 W

1. Use a USB data cable, not a charge-only cable.

2. Press and hold the BOOTSEL button on the Pico 2 W.

3. While holding the button, plug the Pico 2 W into your computer.

4. When the computer detects the board, release the BOOTSEL button.

5. Open Thonny and select the Pico interpreter.

## Installing MicroPython Firmware

6. Go to:

Tools > Options > Interpreter

7. Set the interpreter to:

MicroPython (Raspberry Pi Pico)

8. Connect the Pico 2 W in BOOTSEL mode:

- Disconnect the Pico 2 W from the computer.

- Press and hold the BOOTSEL button.

- While holding BOOTSEL, plug the Pico 2 W into the computer.

- Release the BOOTSEL button when the board appears as a drive.

9. Click Install or update MicroPython.

10. In the installation window, check these options:

- Target volume: The Pico drive shown by your computer

- MicroPython family: RP2

- Variant: Raspberry Pi Pico 2 W

- Version: Choose the latest stable version shown by Thonny

11. Click Install.

12. Wait until the installation is complete. Do not unplug the Pico during installation.

13. Close the installation window.

14. In Thonny, select the Pico interpreter again if needed, then click OK.

15. Your Pico 2 W is now ready for MicroPython programming.

| **FIRMWARE NOTE:** Firmware options can change over time. Use the latest stable official MicroPython firmware for the Raspberry Pi Pico 2 W when preparing a class set of boards. |
| --- |

## Running and Saving Programs

**1.** Type your code in the editor area.

**2.** Click the green Run button.

**3.** Save to the computer first for backup.

**4.** Read program output in the Shell.

**5.** Use File > Save As > Raspberry Pi Pico to save a copy on the board.

**6.** Save as main.py only when the program should run automatically on power-up.

## File Structure Basics

| **File or folder** | **Purpose** |
| --- | --- |
| main.py | Runs automatically when the Pico starts. |
| boot.py | Advanced startup file. Beginners should avoid editing it unless instructed. |
| lib/ | Folder used to store extra libraries. |
| project_name.py | A regular project file run from Thonny. |

**Example file names**

| project_01_led_blink.py project_02_button_input.py project_05_pir_motion_alarm.py main.py |
| --- |

# 5. Library Installation Guide

Many beginner projects use only built-in MicroPython modules such as machine and time. Some projects, such as OLED displays or special sensors, may require extra library files.

## Where Libraries Go

**Typical Pico file structure**

| Raspberry Pi Pico 2 W/  main.py  lib/  example_library.py |
| --- |

## How to Add a Library File

**1.** Download or prepare the required .py library file from a trusted source.

**2.** Open Thonny and connect the Pico.

**3.** Create a folder named lib on the Pico if it does not already exist.

**4.** Upload the library file into the lib folder.

**5.** Import the library in your project code.

## Common Import Issues

| **Problem** | **Possible cause** | **Solution** |
| --- | --- | --- |
| ImportError | Library file is missing or named incorrectly. | Check spelling and upload the file to the Pico. |
| Wrong folder | Library was saved on the computer instead of the Pico. | Use Thonny file browser to confirm the file is on the Pico. |
| Wrong file name | Import name does not match the file name. | If the file is ssd1306.py, import ssd1306. |
| Unsupported library | The library was written for regular Python. | Use a MicroPython-compatible library. |