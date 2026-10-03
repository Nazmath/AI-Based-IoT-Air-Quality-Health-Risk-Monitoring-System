# AI IoT Air Quality Monitor

ESP32 + MQTT + Python ML project for real-time indoor air-quality risk classification.

## Features
- ESP32 firmware for DHT22 and MQ-135 style sensors
- MQTT telemetry
- Synthetic dataset generator for safe development without hardware
- Random Forest air-quality risk classifier
- Real-time MQTT inference service
- Streamlit dashboard
- Wokwi-ready wiring guide

## Architecture
ESP32 -> MQTT broker -> Python inference -> Streamlit dashboard

## Risk classes
- LOW
- MODERATE
- HIGH
- CRITICAL

The model is a portfolio/demo classifier, not a certified medical or environmental measurement system.

## Quick start
1. Install Mosquitto or use a local/public MQTT broker you control.
2. `python -m venv .venv`
3. Activate the environment.
4. `pip install -r requirements.txt`
5. `python ai/generate_dataset.py`
6. `python ai/train_model.py`
7. Start MQTT subscriber: `python mqtt/mqtt_subscriber.py`
8. Start dashboard: `streamlit run dashboard/app.py`
9. Configure `esp32/config.h` and flash `esp32/air_quality_monitor.ino`.

## Demo without ESP32
Run `python mqtt/simulator.py` to publish realistic sample telemetry to MQTT.

## Project structure
See the repository tree for firmware, ML, MQTT, dashboard, data, reports, and Wokwi documentation.
