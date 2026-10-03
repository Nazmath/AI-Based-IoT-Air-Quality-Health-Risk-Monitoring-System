import json
from pathlib import Path
import joblib
import paho.mqtt.client as mqtt
from settings import MQTT_HOST, MQTT_PORT, MQTT_TOPIC, MQTT_CLIENT_ID

ROOT = Path(__file__).resolve().parents[1]
MODEL = joblib.load(ROOT / "ai" / "model" / "air_quality_model.joblib")
FEATURES = ["temperature_c", "humidity_pct", "gas_index", "pm25_ugm3"]
OUT = ROOT / "data" / "live_predictions.jsonl"

def classify(payload):
    x = [[float(payload[k]) for k in FEATURES]]
    return MODEL.predict(x)[0]

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected:", reason_code)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        payload["risk"] = classify(payload)
        with OUT.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload) + "\n")
        print(payload)
    except Exception as exc:
        print("Message error:", exc)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=MQTT_CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_forever()
