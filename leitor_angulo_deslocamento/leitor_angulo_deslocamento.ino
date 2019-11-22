#include <AS5045.h>

// Pinos de comunicaçao do Arduino
#define CSpin   2
#define CLKpin  3
#define DOpin   4

AS5045 enc (CSpin, CLKpin, DOpin);
float initial_angle;
float read_angle;

void setup ()
{
  Serial.begin (115200);
  if (!enc.begin ()) Serial.println ("Error setting up AS5045");
  delay(200);
  initial_angle = enc.read() * 0.08789;        
}

void loop ()
{
  read_angle = enc.read() * 0.08789;
  if(read_angle < initial_angle) {
    Serial.println (360 - initial_angle + read_angle, DEC);
  } else {
    Serial.println (read_angle - initial_angle, DEC);
  }
  delay(10);
}
