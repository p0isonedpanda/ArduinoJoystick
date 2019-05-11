#include <ArduinoJson.h>

StaticJsonDocument<200> info;

int joyButton = 7;
int joyX = 0;
int joyY = 1;

void setup() {
  // put your setup code here, to run once:
  pinMode(joyX, INPUT);
  pinMode(joyY, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  info["x"] = analogRead(joyX) / 4 - 128;
  info["y"] = analogRead(joyY) / 4 - 128;

  serializeJson(info, Serial);
  Serial.println("");
  delay(100);
}
