# Project 1:LED Control with Arduino and Push Button

| **Description** |You will learn how to create a simple circuit using a Push button and 5 LEDs.
|
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use case** | Demonstrates basic control systems and digital input/output handling. 

## Components (Things You will need)

| ![LED ](../../../docs/manuals/assets/components/LED.png) | ![Arduino Uno](../../../docs/manuals/assets/components/arduino.png) | ![Arduino USB Cable](../../../docs/manuals/assets/components/USB_Cable.png) | ![Breadboard](../../../docs/manuals/assets/components/breadboard.png) | ![Jumper Wires](../../../docs/manuals/assets/components/jump_wire.png) | ![Push Button](../../../docs/manuals/assets/components/Push_Button.png) |
| ---------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------- |

## Building the circuit

Things Needed:

- Arduino Uno = 1
- Arduino USB cable = 1
- Resistor = 1
- Push button = 1
- LEDS = 5
- jumper wires = 12


## Mounting the component on the breadboard

**Step 1.0:** The push button has four unassigned pins.On the middle section of the breadboard,locate each horizontal section lettered A to J.Take the push button and insert two pins into the lettered section ‘g’ horizontally.
Insert the other two pins into the lettered section ‘d’ horizontally.
![inseting push button](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/image%201.png).

**step 2.0:** Inset five (5) LEDs on the breadboard as shown in the picture below.
![inseting push button](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/image%202.png).

## WIRING THE CIRCUIT

### Things Needed:

- Red male-male-to-male jumper wires = 2
- White male-to-male jumper wires = 5
- Green male-to-male jumper wires = 1
- Yellow male-to-male jumper wires = 1
- Black male-to-male jumper wires = 1
- Blue male-to-male jumper wires = 2

**step 1:** Take the Red male-male-to-male jumper wire and place one side of the wire pin under the push button pin located on the lettered section ‘d’ and the other side of the wire pin to the digital pin 2 on the Arduino uno board.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%201.png).

**step 2:** Take the Black male-male-to-male jumper wire and place one side of the wire pin under the other push button pin located on the lettered section ‘d’ and the other side of the wire pin to GND on the Arduino uno board.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%202.png).

**step 3:**Take the Red male-male-to-male jumper wire and place one side of the wire pin under the Positive pin of the Red LED and the other side of the wire pin to the digital pin 3 on the Arduino uno board.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%203.png).

**step 4:** Take the White male-male-to-male jumper wire and place one side of the wire pin on the Negative horizontal section on the breadboard and the other side of the wire pin to GND on the Arduino uno board. This allows for the negative section to be used as a substitute for GND when mounting multiple components.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%204.png).

**step 5:** Take the White male-male-to-male jumper wire and place one side of the wire pin under the Negative pin of the Red LED and the other side of the wire pin to the Negative horizontal section on the breadboard.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%205.png).

**step 6:** Take the Yellow male-male-to-male jumper wire and place one side of the wire pin under the Positive pin of the Yellow LED and the other side of the wire pin to the digital pin 4 on the Arduino uno board.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%206.png).

**step 7:** Take the White male-male-to-male jumper wire and place one side of the wire pin under the Negative pin of the Yellow LED and the other side of the wire pin to the Negative horizontal section on the breadboard.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%207.png).

**step 8:** Take the Green male-male-to-male jumper wire and place one side of the wire pin under the Positive pin of the Green LED and the other side of the wire pin to the digital pin 5 on the Arduino uno board.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%208.png).

**step 9:** Take the White male-male-to-male jumper wire and place one side of the wire pin under the Negative pin of the Green LED and the other side of the wire pin to the Negative horizontal section on the breadboard.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%209.png).

**step 9:** Take the Blue male-male-to-male jumper wire and place one side of the wire pin under the Positive pin of the Blue LED and the other side of the wire pin to the digital pin 6 on the Arduino uno board.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%2010.png).

**step 10:** Take the White male-male-to-male jumper wire and place one side of the wire pin under the Negative pin of the Blue LED and the other side of the wire pin to the Negative horizontal section on the breadboard.
![inseting the buzzer](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/wire%2011.png).

## PROGRAMMING

**Step 1:** Open your Arduino IDE. See how to set up here: [Getting Started](../../../getting-started.md).

**Step 2:** Type the following codes before the void setup function.

``` cpp

const int buttonPin= 2;
int red = 3;
int yellow = 4;
int green = 5;
int blue = 6;
int buttonState= 0;
```

![code 1](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/code%201.png).

**Step 3:** After the void setup ()within the curly brackets type the following codes.

``` cpp
pinMode (buttonPin, INTPUT_PULLUP);
pinMode (red, OUTPUT);
pinMode (yellow, OUTPUT);
pinMode (green, OUTPUT);
pinMode (blue, OUTPUT);
```

![code 2](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/code%202.png).

**Step 4:** : After the (void loop ()) within the curly brackets type

``` cpp
buttonState = digitalRead(buttonPin);
if (buttonState == LOW) {
digitalWrite (red, HIGH);
delay (500);
digitalWrite (red, LOW);
delay (500);
digitalWrite (yellow, HIGH);
delay (500);
digitalWrite (yellow, LOW);
delay (500);
digitalWrite (green, HIGH);
delay (500);
digitalWrite (green, LOW);
delay (500);
digitalWrite (blue, HIGH);
delay (500);
digitalWrite (blue, LOW);
delay (500);
}


```

![code 3](../../../docs/manuals/assets/2.0/2.1.Push%20Button%20+%20LED/4.LED/code%203.png).

## Uploading the code

**Step 1:** Save your code. _See the [Getting Started](../../../getting-started.md) section_

**Step 2:** Select the arduino board and port _See the [Getting Started](../../../getting-started.md) section:Selecting Arduino Board Type and Uploading your code_.

**Step 3:** Upload your code. _See the [Getting Started](../../../getting-started.md) section:Selecting Arduino Board Type and Uploading your code_

## CONCLUSION

If you encounter any problems when trying to upload your code to the board, run through your code again to check for any errors or missing lines of code. If you did not encounter any problems and the program ran as expected, Congratulations on a job well done.
