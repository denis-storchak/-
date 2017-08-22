#include <SoftwareSerial.h>
#define LED1 8
#define LED2 7

String cnt;
int counter = 0;
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
Serial.begin(9600);
while (!Serial) {
}
//Serial.println("Goodnight moon!");
pinMode(LED1, OUTPUT);
pinMode(LED2, OUTPUT);
mySerial.begin(9600);
}

void loop() {

if (mySerial.available())
{
while ((counter < 14) && (mySerial.available()))
{
char symb = (char)mySerial.read();
//Serial.println(symb);
cnt = cnt + symb;
counter++;
}
}

if (Serial.available()) {
mySerial.write(Serial.read());
}

if (counter == 14) {
cnt.remove(0, 1);
cnt.remove(12, 1);
Serial.println(cnt);
// Serial.println("hvuaosj");
cnt = "";
counter = 0;
}

//digitalWrite(LED1, LOW);
//digitalWrite(LED2, LOW);

if (Serial.available()) 
{
// Serial.print("got smth:");
char ledstuff = Serial.read();
//Serial.println(ledstuff);
if(ledstuff == '0') 
{
// Serial.println("0");
digitalWrite(LED1, HIGH);
delay(1500);
digitalWrite(LED1, LOW);
}
else if(ledstuff == '1')
{
//Serial.println("1");
digitalWrite(LED2, HIGH);
delay(1500);
digitalWrite(LED2, LOW);
}

}

}
