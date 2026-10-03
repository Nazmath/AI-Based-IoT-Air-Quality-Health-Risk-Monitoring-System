# Wokwi setup

Use an ESP32 DevKit, DHT22, potentiometer for MQ-135 analog output, and another potentiometer for PM2.5 analog input.

Connections:
- DHT22 DATA -> GPIO 4
- MQ-135 analog -> GPIO 34
- PM2.5 analog simulation -> GPIO 35
- All grounds -> GND
- Sensors -> suitable 3.3 V supply

Replace Wi-Fi and MQTT settings in `esp32/config.h`.

For a Wokwi-only demo, potentiometers can stand in for analog air-quality sensors. This does not represent calibrated PM2.5 or gas concentration.
