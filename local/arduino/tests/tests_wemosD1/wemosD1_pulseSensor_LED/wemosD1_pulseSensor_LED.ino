/*
 * Programa que mapea señal erratica del sensor a 0-100% en un intervalo de 2 segundos
 * luego lo mapea a LED para visualizar latidos
 */

#define RESET_TIME 2000 //Resetea cada 2000ms minimos y maximos
int maxi = 0;
int mini = 1023;
long startTime = 0;
long endTime = 0;

int anterior;
int actual;

void setup() {
  Serial.begin(115200);
  pinMode(A0, INPUT);
  startTime = millis();
  //Serial.println("START");
}

void loop() {
  //Adquisicion
  int raw = analogRead(A0);
  anterior = actual;
  actual = raw;
  int diff = actual - anterior;
  //Procesamiento
  maxi = max(raw, maxi);
  mini = min(raw, mini);
  maxi = mini == maxi ? maxi+10: maxi; 
  endTime = millis();
  long elapsed = endTime - startTime;
  if (elapsed > RESET_TIME){
    startTime = endTime;
    maxi = raw+10;
    mini = raw;
  }
  int mapped = max(min(map(raw, mini, maxi, 0, 200), 200), 0);
  
  //Despliegue
  int pwm = map(mapped, 0, 200, 1023, 0);
  //analogWrite(D4, pwm);
  Serial.print(raw);
  Serial.print(' ');
  Serial.print(mapped);
  Serial.print(' ');
  Serial.println(diff);
  delay(25);
}
