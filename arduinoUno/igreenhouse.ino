#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

int humsuelo = 0;
int lluvia = 0;

void setup()
{
  Serial.begin(9600);
  dht.begin(); 
}

void loop()
{
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  humsuelo = analogRead(0);
  lluvia = analogRead(1);
  Serial.print(";SH:");
  Serial.print(humsuelo);
  Serial.print(";R:");
  Serial.print(lluvia);
  Serial.print(";RT:");
  Serial.print( t );
  Serial.print(";RH:");
  Serial.println( h );
  /*
  Serial.println("---------------------------");
  Serial.print("Moist: " );
  Serial.println(humsuelo);
  Serial.print("Rain: " );  
  Serial.println(lluvia);
  Serial.print("Hum: ");
  Serial.println(h);
  Serial.print("Temp2: ");
  Serial.println(t);*/
  delay(2000);
}
