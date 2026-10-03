from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parents[1]
model = joblib.load(ROOT/"ai"/"model"/"air_quality_model.joblib")
values = [[24.0, 45.0, 60.0, 10.0]]
print(model.predict(values)[0])
