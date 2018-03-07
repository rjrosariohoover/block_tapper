const int analogInPin = A4;
const int trigPin = A3;
const int echoPin = A2;
float an;
float duration, distance;

void setup(){
  //initialize serial communications at 9600 bps:
  Serial.begin(9600);  /* /dev/ttyACM0  */
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop(){
  an = analogRead(A4);
  an = an/4;
  
  analogWrite(3,an);
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = (duration*0.0343)/2;
  
  if(Serial.available() > 0){
   char c = Serial.read();
    if(c=='p'){
      Serial.print(an);
      Serial.print(',');
      Serial.println(distance);
    }
  }
  
  /*if((an >= 30) && (an <= 50)){
    Serial.println("up");
  }
  
  if(an >= 100){
    Serial.println("neutral");
  }
  
  if(an <= 10){
    Serial.println("down");
  }*/
}
