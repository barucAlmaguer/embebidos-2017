/*
 ESP8266 Blink by Simon Peter
 Blink the blue LED on the ESP-01 module
 This example code is in the public domain
 
 The blue LED on the ESP-01 module is connected to GPIO1 
 (which is also the TXD pin; so we cannot use Serial.print() at the same time)
 
 Note that this sketch uses LED_BUILTIN to find the pin with the internal LED
*/

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
