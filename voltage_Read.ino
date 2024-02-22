const int vol=A6;

void setup() {
  // put your setup code here, to run once:
    pinMode(vol,INPUT);
    Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int count=analogRead(vol);
  if(count!=0)
    Serial.println(count);
  else 
    Serial.println(0.001)  ;
}
