#include <Servo.h>
Servo servo;
const int servoPin = 4;

void setup() {
  // attach servo to servoPin then write angle-90 to the pin
  servo.attach(servoPin);
  servo.write(90);
}

void loop() {
}
