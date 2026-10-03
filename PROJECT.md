# Project notes

## What the AI does
The Random Forest classifier maps four sensor features to four demo risk classes. The training data is synthetic and designed to demonstrate the software pipeline.

## Real hardware upgrade
For a real deployment, use a calibrated particulate matter sensor such as a UART PM sensor rather than treating a potentiometer or raw analog MQ reading as a certified concentration. Calibrate sensors and validate the model against labeled measurements.

## Portfolio talking points
- Embedded C/C++ ESP32 firmware
- MQTT telemetry architecture
- Python machine learning pipeline
- Real-time inference
- Streamlit visualization
- Reproducible synthetic dataset generation
