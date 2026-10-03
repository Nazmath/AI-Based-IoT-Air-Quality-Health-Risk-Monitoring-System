#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include "config.h"

#define DHT_PIN 4
#define DHT_TYPE DHT22
#define MQ135_PIN 34
#define PM25_PIN 35

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);
DHT dht(DHT_PIN, DHT_TYPE);

void connectWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) delay(500);
}

void connectMQTT() {
  while (!mqttClient.connected()) {
    String clientId = String(DEVICE_ID) + "-" + String((uint32_t)ESP.getEfuseMac(), HEX);
    bool ok;
    if (strlen(MQTT_USER) > 0) ok = mqttClient.connect(clientId.c_str(), MQTT_USER, MQTT_PASSWORD);
    else ok = mqttClient.connect(clientId.c_str());
    if (!ok) delay(2000);
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectWiFi();
  mqttClient.setServer(MQTT_HOST, MQTT_PORT);
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) connectWiFi();
  if (!mqttClient.connected()) connectMQTT();
  mqttClient.loop();

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int gasRaw = analogRead(MQ135_PIN);
  int pmRaw = analogRead(PM25_PIN);

  if (isnan(temperature) || isnan(humidity)) {
    delay(2000);
    return;
  }

  float gasIndex = (gasRaw / 4095.0f) * 500.0f;
  float pm25 = (pmRaw / 4095.0f) * 150.0f;

  char payload[256];
  snprintf(payload, sizeof(payload),
    "{\"device_id\":\"%s\",\"temperature_c\":%.2f,\"humidity_pct\":%.2f,\"gas_index\":%.2f,\"pm25_ugm3\":%.2f,\"uptime_s\":%lu}",
    DEVICE_ID, temperature, humidity, gasIndex, pm25, millis() / 1000UL);

  mqttClient.publish(MQTT_TOPIC, payload);
  Serial.println(payload);
  delay(5000);
}
