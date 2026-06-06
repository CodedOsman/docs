# Project 3.2.1: SMART SECURITY SYSTEM

| **Description** | This project demonstrates a smart security system using an ultrasonic sensor, a red LED, and a buzzer. The ultrasonic sensor detects nearby objects, and when movement or an object is within a set distance, the red LED turns on and the buzzer activates to provide an alert. |
|------------------|----------------------------------------------------------------|
| **Use case**     | This project can be used in parking systems to detect vehicles approaching a restricted area. When a car gets too close, the LED lights up and the buzzer sounds as a warning signal. |

## Components (Things You will need)

| ![LED](../../../assets/components/leds.webp) | ![Arduino Uno](../../../assets/components/arduino.webp) | ![Arduino USB Cable](../../../assets/components/usbcable.webp) | ![Breadboard](../../../assets/components/breadboard.webp) |![Jumper wires](../../../assets/components/jumperwires.webp)| ![Ultrasonic sensor](../../../assets/components/ultrasonic.webp) | ![Buzzer](../../../assets/components/buzzer.webp) |
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|

## Building the circuit

Things Needed:

-	Arduino Uno = 1
-	Arduino USB cable = 1
-	Red LED = 1
-	Ultrasonic sensor = 1
-	Buzzer = 1
-	Red jumper wire = 1
-	Blue jumper wire = 1
-	Black jumper wires = 2
-	White jumper wire = 1
-	Orange jumper wire = 1
-	Green jumper wire = 1
-	Brown jumper wire =1


## Mounting the component on the breadboard

**Step 1:** Insert the ultrasonic sensor into the breadboard. Then place the red LED into the breadboard beside the buzzer, making sure to identify the positive (long pin) and negative (short pin) correctly.

![LED fixed on breadboard](../../../assets/3.0/Smart_Security_System/circuit_1.png).

## WIRING THE CIRCUIT

**Step 2:** Connect the negative pin of the LED and the negative pin of the buzzer to the GND on the Arduino Uno using jumper wires. Then connect the positive pin of the LED through a resistor to Digital Pin 3, and connect the positive pin of the buzzer to Digital Pin 4 on the Arduino Uno.

![LED fixed on breadboard](../../../assets/3.0/Smart_Security_System/circuit_2.png).

**Step 3:** Connect the ultrasonic sensor to the Arduino Uno by linking the VCC pin to 5V, the GND pin to GND, the TRIG pin to Digital Pin 7, and the ECHO pin to Digital Pin 6 using jumper wires as shown in the circuit setup.

![LED fixed on breadboard](../../../assets/3.0/Smart_Security_System/circuit_3.png).

_**NB:** Make sure you identify where the positive pin (+) and the negative pin (-) is connected to on the breadboard. The longer pin of the LED is the positive pin and the shorter one, the negative PIN_.

_make sure you connect the arduino usb use blue cable to the Arduino board_.

## PROGRAMMING

**Step 1:** Open your Arduino IDE. See how to set up here: [Getting Started](../../Getting Started/Arduino_IDE_Setup.md).

**Step 2:** Type this code as shown by the diagram.
``` cpp
// Pin definitions
Before the void setup() function, type:
const int trigPin = 7;       // HC-SR04 TRIG pin connected to D7
const int echoPin = 6;       // HC-SR04 ECHO pin connected to D6
const int ledPin = 3;        // Red LED connected to D3
const int buzzerPin = 4;     // Buzzer connected to D4
```
![Begin Here](../../../assets/3.0/Smart_Security_System/code_1.PNG).

**Step 3:** Type this code as shown by the diagram.
``` cpp
void setup() {
 // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);  // Set TRIG pin as output
  pinMode(echoPin, INPUT);   // Set ECHO pin as input
  pinMode(ledPin, OUTPUT);   // Set LED pin as output
  pinMode(buzzerPin, OUTPUT);// Set Buzzer pin as output
  Serial.begin(9600);        // Initialize serial communication

}
```
![Begin Here](../../../assets/3.0/Smart_Security_System/code_2.PNG).

**Step 2:** Type this code as shown by the diagram.

```cpp
void loop() { 
 // put your main code here, to run repeatedly:
 long duration, distance;
  
  // Clear the TRIG pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Set the TRIG pin HIGH for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the ECHO pin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance
  distance = (duration / 2) / 29.1; // Convert to centimeters
  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Check if the distance is within the threshold
  if (distance < 50) { // Threshold distance in cm
    digitalWrite(ledPin, HIGH);   // Turn on LED
    digitalWrite(buzzerPin, HIGH);// Turn on Buzzer
  } else {
    digitalWrite(ledPin, LOW);    // Turn off LED
    digitalWrite(buzzerPin, LOW); // Turn off Buzzer
  }
  
  delay(500); // Wait for half a second before next reading
}
  ```
![LED fixed on breadboard](../../../assets/3.0/Smart_Security_System/code_3.PNG).

**Step 4:** Save your code. _See the [Getting Started](../../Getting Started/Arduino_IDE_Setup.md) section_

**Step 5:** Select the arduino board and port _See the [Getting Started](../../Getting Started/Arduino_IDE_Setup.md) section:Selecting Arduino Board Type and Uploading your code_.

**Step 6:** Upload your code.

## CONCLUSION
This project demonstrated how an ultrasonic sensor can be used with an Arduino Uno to detect nearby objects and trigger an LED and buzzer as alerts. It helped in understanding distance sensing, object detection, and how sensors can be used in simple security and warning systems.


