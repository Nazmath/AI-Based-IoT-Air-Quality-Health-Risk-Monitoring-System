import json, random, time
import paho.mqtt.client as mqtt
from settings import MQTT_HOST, MQTT_PORT, MQTT_TOPIC

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="air-quality-simulator")
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_start()

while True:
    scenario = random.choices(["clean", "moderate", "polluted"], weights=[0.55, 0.30, 0.15])[0]
    if scenario == "clean":
        t, h, g, p = random.gauss(24, 2), random.gauss(48, 5), random.gauss(65, 15), random.gauss(12, 4)
    elif scenario == "moderate":
        t, h, g, p = random.gauss(28, 3), random.gauss(58, 7), random.gauss(180, 35), random.gauss(40, 10)
    else:
        t, h, g, p = random.gauss(32, 4), random.gauss(70, 8), random.gauss(360, 45), random.gauss(90, 18)
    data = {"device_id":"SIM-01", "temperature_c":round(t,2), "humidity_pct":round(h,2), "gas_index":round(max(g,0),2), "pm25_ugm3":round(max(p,0),2), "uptime_s":int(time.time())}
    client.publish(MQTT_TOPIC, json.dumps(data))
    time.sleep(3)
