# Project 1: Ultrasonic distance sensor with traffic light module.

| **Description** | This smart lighting system illustrate the potential of using Arduino, LEDs and ultrasonic sensor in infrastructure and street light planning. |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use case**    | Imagine you want to control the flow traffic and the specific time the traffic light turns on using the distance of cars on the road.         |

## Components (Things You will need)


| ![Arduino Uno](../../../docs/manuals/assets/components/arduino.png) | ![Arduino USB Cable](../../../docs/manuals/assets/components/USB_Cable.png) | ![Jumper Wires](../../../docs/manuals/assets/components/jump_wire.png) | ![Breadboard](../../../docs/manuals/assets/components/breadboard.png) |![Ultrasonic Sensor](../../../docs/manuals/assets/components/ultrasonic.png)| ![Traffic Light Module](../../../docs/manuals/assets/components/trafficmodule.png)|
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------| -------------------------|


## Building the circuit

Things Needed:

- Arduino Uno = 1
- Arduino USB cable = 1
- Jumper wires
- ultrasonic Sensor = 1
- Breadboard = 1
- Traffic Light Module = 1

## Mounting the component on the breadboard

- Breadboard = 1
- Traffic Light Module = 1
- Ultrasonic sensor = 1

**Step 1:** • The ultrasonic distance sensor has four pins (Echo, Trig, VCC and GND), On the middle section of the breadboard, locate each horizontal section lettered A to J. Take the ultrasonic distance sensor and insert it into any of the lettered section (Say A) horizontally.

![Mount the ultrasonic Sensor on the Breadboard](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Picture1.jpg).

**Step 2:** The Traffic light module has four pins Red(R), Yellow(Y), Green(G) and GND. On the middle section of the breadboard, locate each horizontal section lettered A to J. Take the Traffic Light module and insert it into any of the lettered section (Say A) horizontally.

![Mount the Traffic Light on the Breadboard](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/traffic.jpg).

**NB:**Take note of where each of the pins are placed on the bread board.

## WIRING THE CIRCUIT

### Things Needed:

- Red male-male-to-male jumper wires = 2
- White male-to-male jumper wires = 2
- Green male-to-male jumper wires = 2
- Yellow male-to-male jumper wires = 2
- Arduino Uno Board

**Step 1:** Take the Red male-male-to-male jumper wire and place one side of the wire pin under the Echo pin of the ultrasonic distance sensor and the other side of the wire pin to the digital pin 2 on the Arduino uno board.

![connect red jumper wire](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/red.jpg).

**NB:**Take note of the digital pin you allocated to the Echo pin.

**Step 2:** Take the Green male-male-to-male jumper wire and place one side of the wire pin under the Trig pin of the ultrasonic distance sensor and the other side of the wire pin to the digital pin 3 on the Arduino uno board.

![connect green jumper wire](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/green.jpg).

**NB:**Take note of the digital pin you allocated to the trig pin.

**Step 3:** Take the Blue male-male-to-male jumper wire and place one side of the wire pin under the VCC pin of the ultrasonic distance sensor and the other side of the wire pin to the 5V pin on the Arduino uno board.

![connect blue jumper wire](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/blue.jpg).

**Step 4:** Finally, Take the White male-male-to-male jumper wire and place one side of the wire pin under the GND pin of the ultrasonic distance sensor and the other side of the wire pin to the GND port on the Arduino Uno Board.

![connect white jumper wire](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/white.jpg).

**Step 5:** Take the Red male-to-male jumper wire and place one side of the wire pin under the Red pin of the traffic light module and the other side of the wire pin to the digital pin 4 on the Arduino uno board.

![connect red jumper wire to traffic](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Tred.jpg).

**NB:**Take note of the digital pin you allocated to the Positive pin.

**Step 6:** Take the Green male-to-male jumper wire and place one side of the wire pin under the Green pin of the traffic light module and the other side of the wire pin to the digital pin 5 on the Arduino uno board.

![connect green jumper wire to traffic](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Tgreen.jpg).

**Step 7:** Take the Yellow male-to-male jumper wire and place one side of the wire pin under the Yellow pin of the traffic light module and the other side of the wire pin to the digital pin 6 on the Arduino uno board.

![connect yellow jumper wire to traffic](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Tyellow.jpg).

**Step 8:** Finally, Take the White male-male-to-male jumper wire and place one side of the wire pin under the GND pin of the module and the other side of the wire pin to the GND port on the Arduino Uno Board.

![connect white jumper wire to traffic](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Twhite.jpg).

**Step 9:** Connect the USB port of the Arduino cable to the USB port of your laptop and the other side to the Arduino Uno Board.

![connect USB cable to laptop](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/usb.jpg).

## PROGRAMMING

**Step 1:** Open your Arduino IDE. See how to set up here: [Getting Started](../../../getting-started.md).

**Step 2:** Type `const int Echo = 2; `
as shown below in the picture below: on line one before void Setup() function.

![create Echo variable](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Picture10.png).

**Step 3:** Type `int Trig = 3;  `
as shown below in the picture below: on line one before void Setup() function.

![create Trig variable](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Picture11.png).

**Step 4:** Type `int Red = 4; `
as shown below in the picture below: on line one before void Setup() function.

![create Red Light variable](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Lred.png).

**Step 5:** Type `int Green  = 5; `
as shown below in the picture below: on line one before void Setup() function.

![create yellow Light variable](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Lgreen.png).

**Step 6:** Type `int Yellow = 6; `
as shown below in the picture below: on line one before void Setup() function.

![create Green Light variable](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Lyellow.png).

**Step 7:** Type `long duration; ` and Type ` long duration;`
as shown below in the picture below: on line one before void Setup() function.

![declare duration and distance variable](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/distance.png).

**Step 8:** Type
`const int red_threshold = 10;`
`const int yellow_threshold = 20; `
`const int green_threshold = 5;`

as shown below in the picture below: on line one before void Setup() function.

![create a threshold](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/threshold.png).

**NB:** Make sure you avoid errors when typing. Do not omit any character or symbol especially the bracket {} and semicolons; and place them as you see in the image. The code that comes after the two ash backslashes “//” are called comments. They are not part of the code that will be run, they only explain the lines of code. You can avoid typing them.

**Step 9:** In the {} after the

`pinMode (Echo, INTPUT);`
`pinMode (Trig, OUTPUT); `
`Serial.begin (9600);`
`pinMode (Red, OUTPUT);`
`pinMode (Yellow, OUTPUT);`
`pinMode (Green, OUTPUT);`

as shown below in the picture below:

![initialize the variables](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/initialize.png).

**Step 10:** In the {} after the

`digitalWrite (Trig, LOW); `
`delay (200);`
`digitalWrite (Trig, HIGH); `
`delay (100);`
`digitalWrite (Trig, LOW);`
`duration = pulseIn (Echo, HIGH);`
`distance = duration * 0.034/2;`
as shown below in the picture below:

![Type this void loop](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Picture18.png).

**Step 11:** Type This Function as shown in the image below.

`if (distance == red_threshold)`
`digitalWrite (Red, HIGH); `
`else`
`digitalWrite (Red, LOW); `
`if (distance == yellow_threshold)`
`digitalWrite (Yellow, HIGH); `
`else`
`digitalWrite (Yellow, LOW); `
`if (distance == green_threshold)`
`digitalWrite (Green, HIGH); `
`else`
`digitalWrite (Green, LOW); `
`Serial.print (distance);`
`Serial.println (“cm”);`
`delay (100);`
`distance = duration * 0.034/2; `
as shown in the picture below.

![create a new function](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/function.png).

**Step 12:** Save your code. _See the [Getting Started](../../../getting-started.md) section_

**Step 13:** Select the arduino board and port _See the [Getting Started](../../../getting-started.md) section:Selecting Arduino Board Type and Uploading your code_.

**Step 14:** Upload your code. _See the [Getting Started](../../../getting-started.md) section:Selecting Arduino Board Type and Uploading your code_

**Step 15:** Click on the serial monitor icon to view the amount of sound being recorded as shown in the picture below:

![open the Serial Monitor](../../../docs/manuals/assets/1.0/Sound_Sensor/serial_monitor.png).

## OBSERVATION

![Serial monitor starts displaying distance values](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/Picture20.png)

![The serial monitor recording 20cm](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/20.png)

![project](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/200.jpg)

![The serial monitor recording 10cm](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/10.png)

![The serial monitor recording 20cm](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/100.jpg)

![The serial monitor recording 5cm](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/5.png)

![The serial monitor recording 20cm](../../../docs/manuals/assets/2.0/ultrasonic_Sensor/50.jpg)

## CONCLUSION

If you encounter any problems when trying to upload your code to the board, run through your code again to check for any errors or missing lines of code. If you did not encounter any problems and the program ran as expected, Congratulations on a job well done.
