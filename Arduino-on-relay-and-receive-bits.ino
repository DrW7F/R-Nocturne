const int pinLed = 7;
void setup() {
  Serial.begin(115200);
  pinMode(pinLed, OUTPUT);
  
}

void loop() {
  if (Serial.available()>0)
  {
    char option = Serial.read();
    if (option='1')
    {
      digitalWrite(pinLed, HIGH);
      delay(5000);
      digitalWrite(pinLed, LOW);
      delay(6000);
    }
  }
}
