/*
GETTING STARTED:
http://cyaninfinite.com/tutorials/getting-started-with-the-wemos-d1-esp8266-wifi-board/#Pinouts

*/
int pinMap[] = {};

int led_builtin = D4;
void setup() {
  Serial.begin(9600);
  pinMode(led_builtin, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
  Serial.print("Pin del led:");
  Serial.println(led_builtin);
}

// the loop function runs over and over again forever
void loop() {
  blinky(led_builtin, 50, 100);
  blinky(led_builtin, 50, 1000);
}

void blinky(int pin, int delH, int delL){
  digitalWrite(pin, LOW);   // LED ON (ESP stuff)
  delay(delH);                        
  digitalWrite(pin, HIGH);  //LED off
  delay(delL);  
}
