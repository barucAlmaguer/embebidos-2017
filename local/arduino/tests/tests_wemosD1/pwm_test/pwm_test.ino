void setup() {
  // put your setup code here, to run once:
  pinMode(D4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 1020; i+=5){
    analogWrite(D4, i);
    delay(20);
  }
  for (int i = 1020; i > 0; i-=5){
    analogWrite(D4, i);
    delay(20);
  }
}

void blinky(int pin, int delH, int delL){
  digitalWrite(pin, LOW);   // LED ON (ESP stuff)
  delay(delH);                        
  digitalWrite(pin, HIGH);  //LED off
  delay(delL);  
}
