from pathlib import Path
import json
import pandas as pd
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "data" / "live_predictions.jsonl"
DATA = ROOT / "data" / "air_quality_dataset.csv"

st.set_page_config(page_title="AI IoT Air Quality Monitor", page_icon="🌿", layout="wide")
st.title("🌿 AI IoT Air Quality Monitor")
st.caption("ESP32 telemetry + MQTT + Random Forest risk classification")

if LIVE.exists():
    records = [json.loads(x) for x in LIVE.read_text(encoding="utf-8").splitlines() if x.strip()]
    df = pd.DataFrame(records)
else:
    df = pd.DataFrame()

if not df.empty:
    latest = df.iloc[-1]
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Temperature", f"{latest.temperature_c:.1f} °C")
    c2.metric("Humidity", f"{latest.humidity_pct:.1f} %")
    c3.metric("PM2.5", f"{latest.pm25_ugm3:.1f} µg/m³")
    c4.metric("AI Risk", str(latest.risk))
    chart = px.line(df.tail(100), y=["temperature_c","humidity_pct","gas_index","pm25_ugm3"], markers=True, title="Recent telemetry")
    st.plotly_chart(chart, use_container_width=True)
    st.dataframe(df.tail(30), use_container_width=True)
else:
    st.info("No live MQTT predictions yet. Start mqtt_subscriber.py and simulator.py.")

st.subheader("Model training data")
if DATA.exists():
    train_df = pd.read_csv(DATA)
    st.dataframe(train_df.head(20), use_container_width=True)
