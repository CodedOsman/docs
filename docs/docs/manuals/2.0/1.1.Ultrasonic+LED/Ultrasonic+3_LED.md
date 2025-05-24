# Project 2.002: LED and Ultrasonic Sensor Control 

| **Description** | You will learn how to create a simple circuit using a microcontroller, Three LEDs and an Ultrasonic Sensor. |
|------------------|----------------------------------------------------------------|
| **Use case**     | Imagine you want to use a sensor to measure the distance of an object and turn on or off 2 LEDs alternatively based on the distance measured using Arduino.  |

## Components (Things You will need)

| ![LED](../../assets/components/LED.png) | ![Arduino Uno](../../assets/components/arduino.png) | ![Arduino USB Cable](../../assets/components/USB_Cable.png) | ![Breadboard](../../assets/components/breadboard.png) |![Breadboard](../../assets/components/jump_wire.png)| ![Breadboard](../../assets/components/ultrasonic.png)|
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|

## Building the circuit

Things Needed:

-	Arduino Uno Board = 1
-	Arduino USB Cable = 1
-	Breadboard = 1
-	Red Jumper Wire = 1
-	Black Jumper Wire = 1
-	White Jumper Wire = 1
-	Blue Jumper Wire = 1
-	Green Jumper Wire = 2
-	Brown Jumper Wire = 1
-	Violet Jumper Wire = 1
-	Orange Jumper Wire = 1
-	Grey Jumper Wire
-	Yellow Jumper wire
-	Red LED = 1
-	Green LED = 1
-	White LED = 1
-	Ultrasonic Sensor = 1


## Mounting the component on the breadboard

### Things needed:
-	Ultrasonic Sensor = 1
-	Breadboard =1
- 	Red LED = 1
-  Green LED = 1
-  White LED = 1

**Step 1:** Take the breadboard and the ultrasonic sensor. Insert the ultrasonic sensor into the horizontal connectors on the breadboard, with the pins facing outwards as shown in the picture below

![Ultrasonic sensor fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/ultrasonic_on_breadboard.jpg).

**Step 2:** Insert the red LED into the horizontal connectors on the breadboard beside the ultrasonic sensor and take note of where the positive pin (long pin) is and where the negative pin (short pin) is as shown in the picture below.

![red LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/ultrasonic_led.jpg).

**Step 3:** Insert the LED green into the horizontal connectors on the breadboard on the other side of the ultrasonic sensor and take note of where the positive pin (long pin) is and where the negative pin (short pin) is as shown in the picture below.

![green LED fixed on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_1.jpg).

**Step 4:** Insert the White LED into the horizontal connectors on the breadboard and take note of where the positive pin (long pin) is and where the negative pin (short pin) is as shown in the picture below.

![white LED fixed on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_2.jpg).

## WIRING THE CIRCUIT

### Things Needed:

-	Red male-to-male jumper wire = 1
-	Black male-to-male jumper wire = 1
-	White male-to-male jumper wire = 1
-	Blue male-to-male jumper wire = 1
-	Brown male-to-male jumper wire = 1
-	Green male-to-male Jumper Wire = 1
-	Violet male-to-male Jumper Wire = 1
-	Orange male-to-male Jumper Wire = 1

**Step 1:** Connect one end of the red male-to-male jumper wire to the VCC pin of the Ultrasonic sensor and the other end to the 5V pin on the Arduino Uno board as shown in the picture below.

![red wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_3.jpg)

**Step 2:** Connect one end of the black male-to-male jumper wire to the GND pin of the Ultrasonic sensor and the other end to the GND pin on the Arduino Uno board as shown in the picture below.

![black wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_4.jpg).

**Step 3:** Connect one end of the white male-to-male jumper wire to the Trig pin of the Ultrasonic sensor and the other end to digital pin 11 on the Arduino Uno board as shown in the picture below.

![white wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_5.jpg).

**Step 4:** Connect one end of the Blue male-to-male jumper wire to the Echo pin of the Ultrasonic sensor and the other end to digital pin 12 on the Arduino Uno board as shown in the picture below.

![blue wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_6.jpg).

**Step 5:** Connect one end of the brown male-to-male jumper wire to the negative pin of the LED and the other end to digital pin GND on the Arduino Uno board as shown in the picture below.

![brown wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_7.jpg).

**Step 6:** Connect one end of the green male-to-male jumper wire to the positive pin of the LED and the other end to pin 13 on the Arduino Uno board as shown in the picture below.

![green wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_8.jpg).

**Step 7:** Connect one end of the violet male-to-male jumper wire to the positive pin of the LED and the other end to pin 10 on the Arduino Uno board as shown in the picture below.

![violet wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_9.jpg).

**Step 8:** Connect one end of the orange male-to-male jumper wire to the negative pin of the green LED and the other end to the line of holes labelled negative on the breadboard as shown in the picture below.

![orange wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_10.jpg).

**Step 9:** Connect one end of the gray male-to-male jumper wire to the positive pin of the white LED and the other end to digital pin 9 on the Arduino Uno board as shown in the picture below.

![gray wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_11.jpg).

**Step 10:** Connect one end of the yellow male-to-male jumper wire to the negative pin of the white LED and the other end to the port next to the orange male-to-male jumper wire on the breadboard to connect to the GND as shown in the picture below.

![yellow wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_12.jpg).

**Step 11:** Connect one end of the green male-to-male jumper wire to the GND of the Arduino Uno board and the other end to the negative section of the Breadboard to power the whole negative section as shown in the picture below.

![yellow wire on breadboard](../../assets/2.0/1.3.Ultrasonic+3LED/circuit_13.jpg).

## PROGRAMMING

**Step 1:** Open your Arduino IDE. See how to set up here: [Getting Started](../../../../README.md#getting-started).

**Step 2:** ```const int Echo = 12;``` to define the Echo pin.

![Code 1](../../assets/2.0/1.1.Ultrasonic+LED/code_1.png).

_**NB:** Make sure you avoid errors when typing. Do not omit any character or symbol especially the bracket {} and semicolons; and place them as you see in the image. The code that comes after the two ash backslashes “//” are called comments. They are not part of the code that will be run, they only explain the lines of code. You can avoid typing them._

**Step 3:** Type ```const int Trig = 11;``` to define the Trig pin.

![Code 2](../../assets/2.0/1.1.Ultrasonic+LED/code_2.png).

**Step 4:** Press ENTER to go to the next line, type ```const int led = 13;``` to define the pin for the led

![Code 3](../../assets/2.0/1.1.Ultrasonic+LED/code_3.png).

**Step 5:** Press ENTER to go to the next line, type ```const int led_2 = 10;``` to define the second pin for the led

![Code 4](../../assets/2.0/1.2.Ultrasonic+2LED/code_1.png).

**Step 6:** Press ENTER to go to the next line, type ```const int led_3 = 9;``` to define the third pin for the led

![Code 5](../../assets/2.0/1.3.Ultrasonic+3LED/code_1.png).

**Step 7:** Press ENTER to go to the next line, type ``` int distance;``` to declare the distance variable.

![Code 6](../../assets/2.0/1.3.Ultrasonic+3LED/code_2.png).

**Step 8:** Type ```long duration;``` to declare the duration variable.

![Code 7](../../assets/2.0/1.3.Ultrasonic+3LED/code_3.png).

**Step 9:** Type ```const int distance_threshold = 20;``` to declare the distance threshold variable.

![Code 8](../../assets/2.0/1.3.Ultrasonic+3LED/code_4.png).

**Step 10:** Inside the curly brackets of the void setup () function, type ```pinMode(Trig, OUTPUT);``` to set the Trig pin as an output.

![Code 9](../../assets/2.0/1.3.Ultrasonic+3LED/code_5.png).

**Step 11:** Type ```pinMode(Echo, INPUT);``` to set the Echo pin as an input.

![Code 10](../../assets/2.0/1.3.Ultrasonic+3LED/code_6.png).

**Step 12:** Type ```Serial.begin (9600);``` As shown in the picture below. This is to activate the serial monitor.

![Code 11](../../assets/2.0/1.3.Ultrasonic+3LED/code_7.png).

**Step 13:** Type ```pinMode(led, OUTPUT);``` As shown in the picture below. This is to activate the serial monitor.

![Code 12](../../assets/2.0/1.3.Ultrasonic+3LED/code_8.png).

**Step 14:** Type ```pinMode(led_2, OUTPUT);``` As shown in the picture below. This is to activate the serial monitor.

![Code 13](../../assets/2.0/1.3.Ultrasonic+3LED/code_9.png).

**Step 15:** Type ```pinMode(led_3, OUTPUT);``` As shown in the picture below. This is to activate the serial monitor.

![Code 14](../../assets/2.0/1.3.Ultrasonic+3LED/code_10.png).

**Step 16:** Inside the curly brackets of the void loop (), which is where you put your code to run repeatedly. Type ```digitalWrite(Trig, LOW);``` As shown in the picture below.

![Code 15](../../assets/2.0/1.3.Ultrasonic+3LED/code_11.png).

**Step 17:** Type ```delay (200);``` to introduce a delay.

![Code 16](../../assets/2.0/1.3.Ultrasonic+3LED/code_12.png).

**Step 18:** Type the following code to turn ON the ultrasonic sensor. As shown in the picture below.
   ```
   digitalWrite (Trig, HIGH);
   delay (100); //to introduce a delay. 
   ```
![Code 17](../../assets/2.0/1.3.Ultrasonic+3LED/code_13.png).

**Step 19:** Type ```digitalWrite (Trig, LOW);``` to turn off the ultrasonic sensor. As shown in the picture below to turn OFF the ultrasonic sensor.

![Code 18](../../assets/2.0/1.3.Ultrasonic+3LED/code_14.png).

**Step 20:** Type the following code
   ```
   duration = pulseIn (Echo, HIGH); // to read the duration from the Echo pin. As shown in the picture below.
   //This is to take input from the Echo pin.

   distance = duration * 0.034 / 2; // to calculate the distance. As shown in the picture below.
   ```

![Code 19](../../assets/2.0/1.3.Ultrasonic+3LED/code_15.png).

**Step 21:** Type the conditional statement to turn on the LED at a distance less than the threshold distance.
   ```
   if (distance < distance_threshold){
      digitalWrite (led, HIGH);
      digitalWrite (led_2, HIGH);
      digitalWrite (led_3, HIGH);
   }
   ```
![Code 20](../../assets/2.0/1.3.Ultrasonic+3LED/code_16.png).

**Step 22:** Type 
   ```
   else{
      digitalWrite (led, LOW);
      digitalWrite (led_2, LOW);
      digitalWrite (led_3, LOW);
   }
   ```

![Code 20](../../assets/2.0/1.3.Ultrasonic+3LED/code_17.png).

**Step 23:** Type the following code to print the distance value to the serial monitor.  As shown in the picture below.

   ```
   Serial.print (distance); //This code allows the serial monitor to print the values for distance.
   Serial.println (“cm”); //Here a unit is given to the distance values.
   delay (100);
   ```

![Code 21](../../assets/2.0/1.3.Ultrasonic+3LED/code_18.png).


**Step 24:** Save your code. _See the [Getting Started](../../../../README.md#getting-started) section_

**Step 25:** Select the arduino board and port _See the [Getting Started](../../../../README.md#getting-started) section:Selecting Arduino Board Type and Uploading your code_.

**Step 26:** Upload your code. _See the [Getting Started](../../../../README.md#getting-started) section:Selecting Arduino Board Type and Uploading your code_

## OBSERVATION

**Step 1:** Click on the serial monitor icon to view the distances being recorded as shown in the picture below.

![Observation 1](../../assets/2.0/1.2.Ultrasonic+2LED/observation_1.png).

**Step 2:** Put an object or your hand in front of the ultrasonic sensor and keep moving it away or closer to see the changes in the distances on the serial monitor and the LED turning ON and OFF as per the distances. As shown in the pictures below.

![Observation 2](../../assets/2.0/1.2.Ultrasonic+2LED/observation_2.png).

![Observation 4](../../assets/2.0/1.3.Ultrasonic+3LED/observation.jpg).

## CONCLUSION
If you encounter any problems when trying to upload your code to the board, run through your code again to check for any errors or missing lines of code. If you did not encounter any problems and the program ran as expected, Congratulations on a job well done.  
