# Project 3.001: SMART STREET LIGHT (1 LED)

| **Description** | You will learn how to detect the presence or absence of light.  |
|------------------|----------------------------------------------------------------|
| **Use case**     | Controlling visibility of light in streetlights at different times of the day.  |

## Components (Things You will need)

| ![LED](../../../docs/manuals/assets/components/buzzer_ima.webp) | ![Arduino Uno](../../../docs/manuals/assets/components/arduino.png) | ![Arduino USB Cable](../../../docs/manuals/assets/components/USB_Cable.png) | ![Breadboard](../../../docs/manuals/assets/components/breadboard.png) |![Jumper Wires](../../../docs/manuals/assets/components/jump_wire.png)| ![LDR Sensor](../../../docs/manuals/assets/components/ldr.png)|
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|

## Building the circuit

Things Needed:

-	1 Arduino Uno 
-	1 Arduino USB cable 
-	1 Light dependent resistor   
-	1 Red LED 
-	1 Breadboard 
-	1 Red jumper wire 
-	1 Black jumper wire 
-	1 Green jumper wire 
-	1 White jumper wire 
-	1 Brown male-to-male Jumper Wire 
-	1 Blue male-to-male Jumper Wire 

## Mounting the component on the breadboard

### Things needed:

-	1 Light dependent resistor  
-	1 Red LED 
-	1 Breadboard 

**Step 1:** Take the light dependent resistor and the breadboard, insert the light dependent resistor into the horizontal connectors on the   breadboard.

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.2.LDR+Buzzer/circuit_1.jpg).

**Step 2:** Insert the red LED into the horizontal connectors on the breadboard beside the LDR module and take note of where the positive pin (long pin) is and where the negative pin (short pin) is as shown in the picture below.

![Red LED fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED4/circuit_2.jpg).


## WIRING THE CIRCUIT

### Things Needed:

-	1 Red male-to-male jumper wire 
-	1 Black male-to-male jumper wire 
-	1 White male-to-male jumper wire 
-	1 Brown male-to-male jumper wire 
-	1 Green male-to-male Jumper Wire 
-	1 Blue male-to-male Jumper Wire 

**Step 1:** Take the green jumper wire. Connect one end of the wire to the “VCC” port on the LDR module and the other end to the “5V” port on the Arduino UNO board. As shown in the picture below.

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-1.png).

**Step 2:** Take the black jumper wire, connect one end of the wire to the “GND” port on the Arduino UNO board and the other end to the “GND” port on the LDR module. As shown in the picture below

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-2.png).

**Step 3:** Take the violet jumper wire, connect one end of the wire to the “DO” pin of the LDR module and the other end to the digital pin 8 on the Arduino UNO board. As shown in the picture below.

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-3.png).

**Step 4:** Take the brown jumper wire, connect one end of the wire to the “AO” port on the Arduino UNO board and the other end of the pin to the “AO” pin of the LDR module.

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-4.png).

**Step 5:** Take the orange jumper wire.  Connect one end of the wire to the negative pin of the red LED and connect the other end to GND pin on the Arduino UNO board. As shown in the picture below.

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-5.png).

**Step 6:** Take the red jumper wire, connect one end of the wire to the positive pin of the red LED and connect the other end to digital pin 5 on the Arduino UNO board. As shown in the picture below.

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-6.png).


## PROGRAMMING

**Step 1:** Open your Arduino IDE. See how to set up here: [Getting Started](../../../getting-started.md).

**Step 2:** Type ```const int LDR_PIN = A0.```   as shown below in the image 
_**NB:** Make sure you avoid errors when typing. Do not omit any character or symbol especially the bracket { }  and semicolons ;  and place them as you see in the image . The code that comes after the two ash backslashes “//” are called comments. They are not part of the code that will be run, they only explain the lines of code. You can avoid typing them._

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-7.png).

**Step 3:** Type ```const int DO_PIN = 2;``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-8.png).

**Step 4:** Type ```const int LED = 6; ``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-9.png)

**Step 5:** Type ```pinMode (LED, OUTPUT); ;``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-10.png).

**Step 6:** Type ```pinMode (DO_PIN, INPUT); ``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-11.png).

**Step 7:** Type ```Serial.begin(9600);  ``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-12.png).

**Step 8:** Type ```int ldrValue = analogRead (LDR_PIN);   ``` as shown below in the image
![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-13.png).

**Step 9:** Type ```int digitalValue = digitalRead (DO_PIN); ``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-14.png).

**Step 10:** Type ```Serial.print(“Analog Value:”); ``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-15.png).

**Step 11:** Type ```Serial.printIn(IdrValue);``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-16.png).

**Step 12:** Type ```Serial.print (“Digital Value:”);``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-17.png).

**Step 13:** Type 

    ``` cpp
   Serial.printIn(digitalValue)     
    ``` 
    as shown below in the image
![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-18.png).

**Step 14:** Type ``` If (digitalValue < 1) ``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-19.png).

**Step 15:** Type ``` {digitalWrite (LED, HIGH); ```
} as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-20.png).

**Step 16:** Type ```else {digitalWrite (LED, LOW);}``` as shown below in the image

![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-21.png).


![LDR sensor fixed on breadboard](../../../docs/manuals/assets/2.0/3.1.LDR+LED/LDR_and_LED1/image-22.png).



**Step 21:** Save your code. _See the [Getting Started](../../../getting-started.md) section_

**Step 22:** Select the arduino board and port _See the [Getting Started](../../../getting-started.md) section:Selecting Arduino Board Type and Uploading your code_.

**Step 23:** Upload your code. _See the [Getting Started](../../../getting-started.md) section:Selecting Arduino Board Type and Uploading your code_

## Conclusion

If you encounter any problems when trying to upload your code to the board, run through your code again to check for any errors or missing lines of code. If you did not encounter any problems and the program ran as expected Congratulations on a job well done.
