//Gmail notifier 
 
int outPin = 3;
int mail = LOW;
int val;
 
void setup()
{
  pinMode(outPin, OUTPUT);
  Serial.begin(9600);
  Serial.flush();
}
 
void loop()
{
  if (Serial.available())
  {
    val = Serial.read();
    Serial.println(val);
    if (val == 'M') mail = HIGH;
    else if (val == 'N') mail = LOW;
  }
 
  digitalWrite(outPin, mail);
}