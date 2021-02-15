// get servo library for arduino
#include <Servo.h>


// create the servos using servo class
Servo ServoYaw, ServoPitch;

// set servo pins
int servo_pin1 = 3;
int servo_pin2 = 4;

// variables for getting coordinates
String yaw;
String pitch;

void setup() {
  // Serial set bits per second rate
  Serial.begin(115200);
  Serial.setTimeout(10);

  // attach pins
  ServoYaw.attach(servo_pin1);
  ServoPitch.attach(servo_pin2);
};

void loop() {
  // put your main code here, to run repeatedly:
  servoMove();
//  exit(0);
};

void servoMove(){
  if(Serial.available() > 0){
    yaw = Serial.readStringUntil('\n');
    pitch = Serial.readStringUntil('\n');
    ServoPitch.write(pitch.toInt());
    ServoYaw.write(yaw.toInt());
  }
};
