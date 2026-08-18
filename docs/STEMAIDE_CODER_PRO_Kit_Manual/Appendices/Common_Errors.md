# Appendix: Common Errors & Compilation Issues (Coder Pro)

This appendix lists common compile-time, upload, and system-level communication errors encountered when working with the advanced components in the STEMAIDE Coder Pro Kit, along with clear directions on how to resolve them.

---

## 1. Compilation & Library Errors (Code Syntax Issues)

These errors occur when the compiler cannot parse your source code due to syntax issues or missing code dependencies.

### `fatal error: HeaderName.h: No such file or directory`
*   **Examples**:
    *   `fatal error: MFRC522.h: No such file or directory`
    *   `fatal error: LiquidCrystal_I2C.h: No such file or directory`
    *   `fatal error: Keypad.h: No such file or directory`
*   **Cause**: The compiler is trying to build code that includes an external library, but the library is not installed in your Arduino IDE libraries directory.
*   **Fix**: 
    1. In the Arduino IDE, go to **Tools** -> **Manage Libraries...** (or press `Ctrl+Shift+I` / `Cmd+Shift+I`).
    2. Search for the library name (e.g., "MFRC522", "LiquidCrystal I2C", or "Keypad").
    3. Find the official version and click **Install**.
    4. Restart or refresh the IDE and compile your code again.

### `error: 'class MFRC522' has no member named 'PCD_Init'`
*   **Cause**: You have written a library member function (method) with incorrect spelling, incorrect capitalization, or you are using an incompatible/outdated version of the library.
*   **Fix**: 
    *   Check for casing typos. C++ is case-sensitive: `pcd_init` or `Pcd_Init` will throw errors, it must be exactly `PCD_Init()`.
    *   Review the library's official documentation or examples (**File** -> **Examples** -> **MFRC522**) to verify the correct API syntax.

### `error: expected primary-expression before ']' token`
*   **Cause**: This frequently happens in Coder Pro projects using matrix keypads or dot matrices. It indicates an error in defining arrays or matrices, such as leaving a bracket empty or omitting commas between elements.
*   **Fix**: Ensure your row/column keypad matrix is initialized correctly:
    ```cpp
    char keys[ROW_NUM][COL_NUM] = {
      {'1','2','3','A'},
      {'4','5','6','B'},
      {'7','8','9','C'},
      {'*','0','#','D'}
    };
    ```

---

## 2. Communication & Bus Protocols Errors

These errors occur when the program compiles and uploads successfully, but the components fail to talk to the Arduino Uno over I2C, SPI, or Serial connections.

### I2C Screen is Lit but Displays No Characters (or Solid Blocks)
*   **Cause**:
    1.  The LCD screen contrast potentiometer (located on the black I2C backpack board on the back of the LCD) is not adjusted properly.
    2.  The I2C address declared in your code is incorrect.
*   **Fix**:
    *   Use a small screwdriver to gently turn the blue contrast potentiometer on the back of the LCD module until characters become visible.
    *   Check the address in your initialization: `LiquidCrystal_I2C lcd(0x27, 16, 2);`. Some LCDs use `0x3F` instead of `0x27`. Run the **I2C Scanner** code (see the [Troubleshooting Appendix](../Troubleshooting/)) to verify the device's actual address.

### RFID Reader Scans Nothing and Serial Monitor Shows `MFRC522 Software Version: 0x00`
*   **Cause**: The RFID module is not communicating with the Arduino Uno. This is usually due to:
    1.  Incorrect SPI pin wiring.
    2.  Unsoldered header pins on the MFRC522 module (loose contact).
*   **Fix**:
    *   Verify that you have wired the SPI pins exactly as required for the Uno: **SCK** to D13, **MISO** to D12, **MOSI** to D11, **SS (SDA)** to D10, and **RST** to D9.
    *   Ensure the headers on your RFID module are properly soldered. Simply pressing wires into the holes without solder will create intermittent connections and SPI communication failure.

### Real-Time Clock (RTC) Displays `2165/165/165 165:165:165` or Stays Stuck in Time
*   **Cause**: The RTC module is not communicating via I2C, or its battery is dead/uninstalled, preventing the clock crystal from ticking.
*   **Fix**:
    *   Verify that SCL is connected to A5 and SDA to A4 on the Uno.
    *   Ensure a CR2032 battery is installed in the RTC holder.
    *   Add verification logic in your `setup()` to confirm the RTC starts:
        ```cpp
        if (!rtc.begin()) {
          Serial.println("Couldn't find RTC");
          while (1);
        }
        if (rtc.lostPower()) {
          rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
        }
        ```

---

## 3. Power-Related & Reset Errors

Projects in the Coder Pro kit integrate high-current loads (like motors and relays) which can disrupt the stable power supply of the microcontroller.

### The Arduino Resets (Runs `setup()` Repeatedly) when a Motor or Servo Activates
*   **Cause**: Motors and servos draw heavy current spikes when starting or changing directions. This draws down the 5V line of the Arduino below its minimum operational threshold, causing a brownout reset.
*   **Fix**:
    *   **External Power**: Power your servo motors or DC motors using an external battery pack or power supply (e.g., 4 AA batteries) rather than drawing directly from the Arduino 5V pin.
    *   **Common Ground**: Link the negative (-) wire of the external battery pack directly to the Arduino's **GND** pin.
    *   **Decoupling**: Connect a capacitor (10µF to 100µF) across the positive and negative power rails of the motor/servo.
