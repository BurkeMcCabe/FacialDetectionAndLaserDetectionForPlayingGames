

#define lightSensor A5
#define lightSensor2 A4

void setup() {
  Serial.begin(9600);
}

void loop() {
  int lightLevel = analogRead(lightSensor);
  int lightLevel2 = analogRead(lightSensor2);
  Serial.print(lightLevel);
  if (lightLevel >= 100){
    Serial.print(" ");
  } else {
    Serial.print("  ");
  }
  Serial.println(lightLevel2);
}
