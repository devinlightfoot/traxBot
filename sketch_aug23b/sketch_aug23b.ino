int enPin = 11;
int in1Pin = 10;
int in2Pin = 9;
int trigPin = 6;
int echoPin = 5;
float duration, distance;
void setup() {
  pinMode(enPin, OUTPUT);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
 digitalWrite(trigPin, LOW); 
 delayMicroseconds(2); 
 digitalWrite(trigPin, HIGH); 
 delayMicroseconds(10); 
 digitalWrite(trigPin, LOW); 
 duration = pulseIn(echoPin, HIGH);
 distance = duration / 58;
 Serial.println(distance);
 analogWrite(enPin, 100);
 if(distance <= 2.5){
   digitalWrite(in1Pin, false);
   digitalWrite(in2Pin, true);
  }
}
