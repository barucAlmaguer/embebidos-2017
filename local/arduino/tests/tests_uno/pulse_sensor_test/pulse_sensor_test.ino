//Programa de ejemplo para sensor de pulsos del corazón
//Blink en base a latidos :o
#define spln(x) Serial.println(x) 
#define sp(x)   Serial.print(x) 

int pulseSensor = A0;
int purplePin = 0;

void setup(){
  Serial.begin(115200);
  pinMode(pulseSensor, INPUT);
}

void loop(){
  int p = analogRead(pulseSensor);
  spln(p);
  delay(100);
}
