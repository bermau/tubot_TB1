// fonctionne sur IDEA Arduino 1.8.5.
// Motor : Vexta : PK248-03A-C13, powered by a 12 V battery.
// Arduino Uno. + Shield ARD-CNC-v3.0 (bought at Gotronic.fr)

// le programme original est de
// https://www.electroniclinic.com/arduino-cnc-shield-v3-0-and-a4988-hybrid-stepper-motor-driver-joystick/

  // Stepper Motor X
  const int stepPin = 2; //X.STEP
  const int dirPin = 5; // X.DIR

  const int WAIT = 1500 ; // µs
 
 void setup() {
 // Sets the two pins as Outputs
 pinMode(stepPin,OUTPUT); 
 pinMode(dirPin,OUTPUT);
 }
 
 void loop() {
 digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
 
 // Makes 200 pulses for making one full cycle rotation
 for(int x = 0; x < 200; x++) {
 digitalWrite(stepPin,HIGH); 
 delayMicroseconds(WAIT); 
 digitalWrite(stepPin,LOW); 
 delayMicroseconds(WAIT); 
 }
 
 delay(1000); // One second delay
 
 digitalWrite(dirPin,LOW); //Changes the rotations direction
 // Makes 400 pulses for making two full cycle rotation
 for(int x = 0; x < 400; x++) {
 digitalWrite(stepPin,HIGH);
 delayMicroseconds(WAIT);
 digitalWrite(stepPin,LOW);
 delayMicroseconds(WAIT);
 }
 delay(2000);
 }
