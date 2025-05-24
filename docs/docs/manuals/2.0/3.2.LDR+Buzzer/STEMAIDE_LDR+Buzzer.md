# Project 2.006: SMART SOUND ALERT SYSTEM 

| **Description** | You will learn how to detect the presence or absence of light. |
|------------------|----------------------------------------------------------------|
| **Use case**     | Controlling visibility of light in streetlights at different times of the day  |

## Components (Things You will need)

| ![LED](../../assets/components/buzzer_ima.webp) | ![Arduino Uno](../../assets/components/arduino.png) | ![Arduino USB Cable](../../assets/components/USB_Cable.png) | ![Breadboard](../../assets/components/breadboard.png) |![Jumper Wires](../../assets/components/jump_wire.png)| ![LDR Sensor](../../assets/components/ldr.png)|
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|

## Building the circuit

Things Needed:

-	Arduino Uno = 1
-	Arduino USB cable = 1
-	Light dependent resistor   = 1
-	Red jumper wire = 1
-	Black jumper wire = 1
-	Green jumper wire = 1
-	White jumper wire = 1

## Mounting the component on the breadboard

### Things needed:

**Step 1:** Take the light dependent resistor and the breadboard, insert the light dependent resistor into the horizontal connectors on the   breadboard.

![LDR sensor fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_1.jpg).

**Step 2:** Take the Buzzer and insert it into the horizontal connectors on the breadboard.

![Buzzer fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_2.jpg).

## WIRING THE CIRCUIT

**Step 1:** Take the red jumper wire. Connect one end of the wire to the “VCC” port on the light dependent resistor and the other end to the “5V” port on the Arduino UNO.

![Red wire fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_3.jpg).

**Step 2:** Take the black jumper wire. Connect one end of the wire to the “GND” hole on the Arduino UNO and the other end to the “GND” port on the light dependent resistor.

![Black wire fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_4.jpg).

**Step 3:** Take the white jumper wire. Connect one end of the wire to the “DO” hole on the resistor and the other end to hole number 2 on the Arduino UNO.

![White wire fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_5.jpg).

**Step 4:** Take the green jumper wire. Connect one end of the wire to the “AO” port on the Arduino UNO to the “AO” port on the light dependent resistor.

![Green wire fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_6.jpg).

**Step 5:** Take the brown jumper wire.  Connect one end of the wire to one of the ports of the longer pin of the LED and connect the other end to hole number 6 on the Arduino UNO.

![Brown wire fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_7.jpg).

**Step 6:** Take the purple jumper wire. Connect one end of the wire to one of the ports of the shorter pin of the LED and connect the other end to the “GND” on the Arduino UNO.

![Purple wire fixed on breadboard](../../assets/2.0/3.2.LDR+Buzzer/circuit_8.jpg).

## PROGRAMMING

**Step 1:** Open your Arduino IDE. See how to set up here: [Getting Started](../../../../README.md#getting-started).

**Step 2:** Type ```const int LDR_PIN = A0.```   as shown below in the image 
_**NB:** Make sure you avoid errors when typing. Do not omit any character or symbol especially the bracket { }  and semicolons ;  and place them as you see in the image . The code that comes after the two ash backslashes “//” are called comments. They are not part of the code that will be run, they only explain the lines of code. You can avoid typing them._

![Code 1](../../assets/2.0/3.2.LDR+Buzzer/code_1.jpg).

**Step 3:** Type ```const int DO_PIN = 2;``` as shown below in the image

![Code 2](../../assets/2.0/3.2.LDR+Buzzer/code_2.jpg).

**Step 4:** Type ```const int LED = 6;``` as shown below in the image

![Code 3](../../assets/2.0/3.2.LDR+Buzzer/code_3.png).

**Step 5:** Type ```pinMode (DO_PIN, INPUT);``` as shown below in the image

![Code 4](../../assets/2.0/3.2.LDR+Buzzer/code_4.png).

**Step 6:** Type ```Serial.begin(9600);``` as shown below in the image

![Code 4](../../assets/2.0/3.2.LDR+Buzzer/code_10.png).

**Step 7:** Type ```int ldrValue = analogRead (LDR_PIN); ``` as shown below in the image

![Code 5](../../assets/2.0/3.2.LDR+Buzzer/code_6.png).

**Step 8:** Type ```int digitalValue = digitalRead (DO_PIN);  ``` as shown below in the image

![Code 6](../../assets/2.0/3.2.LDR+Buzzer/code_7.png).

**Step 9:** Type ```Serial.print(“Analog Value:”);``` as shown below in the image

![Code 7](../../assets/2.0/3.2.LDR+Buzzer/code_8.png).

**Step 10:** Type ```Serial.printIn(ldrValue);``` as shown below in the image

![Code 8](../../assets/2.0/3.2.LDR+Buzzer/code_9.png).

**Step 11:** Type ```Serial.print(“Digital Value:”);``` as shown below in the image

![Code 9](../../assets/2.0/3.2.LDR+Buzzer/code_10.jpg).

**Step 12:** Type ```Serial.println(digitalValue);``` as shown below in the image

![Code 10](../../assets/2.0/3.2.LDR+Buzzer/code_11.jpg).

**Step 13:** Type ```if(ldrValue < 100){``` as shown below in the image

![Code 11](../../assets/2.0/3.2.LDR+Buzzer/code_12.png).

**Step 14:** Type ```digitalWrite(BUZZER, HIGH);}``` as shown below in the image

![Code 12](../../assets/2.0/3.2.LDR+Buzzer/code_13.png).

**Step 15:** Type ```else{digitalWrite(BUZZER, LOW);}``` as shown below in the image

![Code 12](../../assets/2.0/3.2.LDR+Buzzer/code_14.png).

**Step 16:** Save your code. _See the [Getting Started](../../../../README.md#getting-started) section_

**Step 17:** Select the arduino board and port _See the [Getting Started](../../../../README.md#getting-started) section:Selecting Arduino Board Type and Uploading your code_.

**Step 18:** Upload your code. _See the [Getting Started](../../../../README.md#getting-started) section:Selecting Arduino Board Type and Uploading your code_

## Conclusion

If you encounter any problems when trying to upload your code to the board, run through your code again to check for any errors or missing lines of code. If you did not encounter any problems and the program ran as expected, Congratulations on a job well done. You have now learnt how to program a buzzer to go off  in the absence of light. Practice, as they say makes perfect. Continue to work hard and in time you’ll master it.
