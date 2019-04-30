int led = 13;
char chr;
void setup() {
  // put your setup code here, to run once:
  pinMode (led,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available())
  {
    chr=Serial.read();
    if (chr=='1')
    {
      digitalWrite(led,HIGH); delay (300); digitalWrite(led,LOW); delay (300);
    }
    else if (chr=='0')
    {
      digitalWrite(led, LOW); 
    }
    else if (chr == '2')
    {
      digitalWrite(led, HIGH);

    }
    Serial.println();
  }
}
