# Project 2.001: LED and Ultrasonic Sensor Control 

| **Description** | You will learn how to create a simple circuit using a microcontroller, LED and an Ultrasonic Sensor. |
|------------------|----------------------------------------------------------------|
| **Use case**     | Imagine you want to use a sensor to measure the distance of an object and turn on or off and LED based on the distance measured using Arduino. |

## Components (Things You will need)

| ![LED](../../assets/components/LED.png) | ![Arduino Uno](../../assets/components/arduino.png) | ![Arduino USB Cable](../../assets/components/USB_Cable.png) | ![Breadboard](../../assets/components/breadboard.png) |![Breadboard](../../assets/components/jump_wire.png)| ![Breadboard](../../assets/components/ultrasonic.png)|
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|

## Building the circuit

Things Needed:

-	Arduino Uno Board: 1
-	Arduino USB cable: 1
-	Breadboard: 1
-	Red Led : 1
-	Green led: 1
-	Jumper Wire: 1
-	Ultrasonic sensor: 1

## Mounting the component on the breadboard

### Things needed:

**Step 1:**  Connect one end of red male-to-male jumper wire to the VCC pin of the ultrasonic sensor on the breadboard and the other end to 5v on the Arduino UNO as shown below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/).

**Step 2:** Insert the red LED into the horizontal connectors on the breadboard beside the ultrasonic sensor and take note of where the positive pin (long pin) is and where the negative pin (short pin) is as shown in the picture below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/ultrasonic_led.jpg).

## WIRING THE CIRCUIT

### Things Needed:

-	Red male-to-male jumper wire: 1
-	Black male-to-male jumper wire: 1
-	White male-to-male jumper wire: 1
-	Blue male-to-male jumper wire: 1
-	Brown jumper wire: 1
-	Green Jumper Wire: 1

**Step 1:** Connect one end of the red male-to-male jumper wire to the VCC pin of the Ultrasonic sensor and the other end to the 5V pin on the Arduino Uno board as shown in the picture below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/circuit_1.jpg).

**Step 2:** Connect one end of the black male-to-male jumper wire to the GND pin of the Ultrasonic sensor and the other end to the GND pin on the Arduino Uno board as shown in the picture below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/circuit_2.jpg).

**Step 3:** Connect one end of the white male-to-male jumper wire to the Trig pin of the Ultrasonic sensor and the other end to digital pin 11 on the Arduino Uno board as shown in the picture below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/circuit_3.jpg).

**Step 4:** Connect one end of the blue male-to-male jumper wire to the Echo pin of the Ultrasonic sensor and the other end to digital pin 12 on the Arduino Uno board as shown in the picture below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/circuit_4.jpg).

**Step 5:** Connect one end of the green male-to-male jumper wire to the positive pin of the LED and the other end to digital pin 13 on the Arduino Uno board as shown in the picture below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/circuit_5.jpg).

**Step 6:** Connect one end of the brown male-to-male jumper wire to the positive pin of the LED and the other end to the GND pin on the Arduino Uno board as shown in the picture below.

![LED fixed on breadboard](../../assets/2.0/1.1.Ultrasonic+LED/circuit_6.jpg).

## PROGRAMMING

**Step 1:** Open your Arduino IDE. See how to set up here: [Getting Started](../../../../README.md#getting-started).

**Step 2:** ```const int Echo = 12;``` to define the Echo pin.

![Code 1](../../assets/2.0/1.1.Ultrasonic+LED/code_1.png).

**Step 3:** Type ```const int Trig = 11;``` to define the Trig pin.

![Code 2](../../assets/2.0/1.1.Ultrasonic+LED/code_2.png).

**Step 4:** Press ENTER to go to the next line, type ```const int led = 13;``` to define the pin for the led

![Code 3](../../assets/2.0/1.1.Ultrasonic+LED/code_3.png).

**Step 5:** Type ```long duration;``` to declare the duration variable.

![Code 4](../../assets/2.0/1.1.Ultrasonic+LED/code_4.png).

**Step 6:** Type ```int distance;``` to declare the distance variable.

![Code 5](../../assets/2.0/1.1.Ultrasonic+LED/code_5.png).

**Step 7:** Type ```const int distance_threshold = 20;``` to declare the distance threshold variable.

![Code 6](../../assets/2.0/1.1.Ultrasonic+LED/code_6.png).

**Step 8:** Inside the curly brackets of the void setup () function, type ```pinMode(Trig, OUTPUT);``` to set the Trig pin as an output.

![Code 7](../../assets/2.0/1.1.Ultrasonic+LED/code_7.png).

**Step 9:** Type ```pinMode(Echo, INPUT);``` to set the Echo pin as an input.

![Code 8](../../assets/2.0/1.1.Ultrasonic+LED/code_8.png).

**Step 10:** Type ```Serial.begin (9600);``` As shown in the picture below. This is to activate the serial monitor.

![Code 9](../../assets/2.0/1.1.Ultrasonic+LED/code_9.png).

**Step 11:** Type ```pinMode(led, OUTPUT);``` As shown in the picture below. This is to activate the serial monitor.

![Code 10](../../assets/2.0/1.1.Ultrasonic+LED/code_10.png).

**Step 12:** Inside the curly brackets of the void loop (), which is where you put your code to run repeatedly. Type ```digitalWrite(Trig, LOW);``` As shown in the picture below.

![Code 11](../../assets/2.0/1.1.Ultrasonic+LED/code_11.png).

**Step 13:** Type ```delay (200);``` to introduce a delay.

![Code 12](../../assets/2.0/1.1.Ultrasonic+LED/code_12.png).

**Step 14:** Type the following code as shown in the picture below to turn ON the ultrasonic sensor.
   ```
   digitalWrite(Trig, HIGH);
   delay (100); to introduce a delay
   ```

![Code 13](../../assets/2.0/1.1.Ultrasonic+LED/code_13.png).

**Step 15:** Type ```digitalWrite (Trig, LOW);``` to turn off the ultrasonic sensor. As shown in the picture below to turn OFF the ultrasonic sensor.

![Code 14](../../assets/2.0/1.1.Ultrasonic+LED/code_14.jpg).

**Step 16:** Type the following code
   ```
   duration = pulseIn (Echo, HIGH); // to read the duration from the Echo pin. As shown in the picture below.
   //This is to take input from the Echo pin.

   distance = duration * 0.034 / 2; // to calculate the distance. As shown in the picture below.
   ```

![Code 15](../../assets/2.0/1.1.Ultrasonic+LED/code_15.png).

**Step 17:** Type the conditional statement to turn on the LED at a distance less than the threshold distance.
   ```
   if (distance < distance_threshold)
      digitalWrite (led, HIGH); 
   else 
      digitalWrite (led, LOW); 
   ```
![Code 16](../../assets/2.0/1.1.Ultrasonic+LED/code_16.png).

**Step 18:** Type the following code to print the distance value to the serial monitor.  As shown in the picture below.

   ```
   Serial.print (distance); //This code allows the serial monitor to print the values for distance.
   Serial.println (“cm”); //Here a unit is given to the distance values.
   delay (100);
   ```

![Code 17](../../assets/2.0/1.1.Ultrasonic+LED/code_17.png).


**Step 19:** Save your code. _See the [Getting Started](../../../../README.md#getting-started) section_

**Step 20:** Select the arduino board and port _See the [Getting Started](../../../../README.md#getting-started) section:Selecting Arduino Board Type and Uploading your code_.

**Step 21:** Upload your code. _See the [Getting Started](../../../../README.md#getting-started) section:Selecting Arduino Board Type and Uploading your code_


## CONCLUSION
To sum up, the one LED blink project demonstrates a foundational concept in electronics and programming. Through this simple yet illuminating endeavor, learners grasp the essentials of hardware interfacing, coding logic, and timing control. This project lays the groundwork for more advanced explorations while showcasing the transformative power of just a single LED, sparking curiosity and creativity in the world of DIY electronics.
