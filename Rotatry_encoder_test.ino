int pinDT = 3;
int pinCLK = 4;
int LastVal, CLKVal, DTVal;
int count=0;
int pinBrk=5,pinThr=6,pinNitr = 7;
int brake, throttle, nitrous;
String data="";

void setup()
{
  Serial.begin(25000);
  
  pinMode(pinCLK,INPUT);
  pinMode(pinDT,INPUT);
  pinMode(pinBrk,INPUT);
  pinMode(pinThr,INPUT);
  pinMode(pinNitr,INPUT);
  
  LastVal = digitalRead(pinCLK);
  
  digitalWrite(pinBrk,LOW);
  digitalWrite(pinThr,LOW);
  digitalWrite(pinNitr,LOW);
}

void loop()
{
  brake = 0, throttle = 0, nitrous = 0;
  data = "";
  
  CLKVal = digitalRead(pinCLK);
  if(LastVal!=CLKVal)
  {
     DTVal = digitalRead(pinDT);   
     if(DTVal != CLKVal)
     {
        count++;        
     }
     else
     {
        count--;
     }
  }

  if(digitalRead(pinBrk))
    brake = 1;
  if(digitalRead(pinThr))
    throttle = 1;
  if(digitalRead(pinNitr))
    nitrous = 1;
  
  LastVal = CLKVal;
  
  data+=count;
  data+=" ";
  data+=brake;
  data+=" ";
  data+=throttle;
  data+=" ";
  data+=nitrous;
  
  Serial.println(data);
  
}
