from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT/"data"/"air_quality_dataset.csv")
features = ["temperature_c","humidity_pct","gas_index","pm25_ugm3"]
X_train, X_test, y_train, y_test = train_test_split(df[features], df.risk, test_size=.2, random_state=42, stratify=df.risk)
model = RandomForestClassifier(n_estimators=250, random_state=42, class_weight="balanced")
model.fit(X_train, y_train)
pred = model.predict(X_test)
(ROOT/"ai"/"model").mkdir(exist_ok=True)
joblib.dump(model, ROOT/"ai"/"model"/"air_quality_model.joblib")
report = f"Accuracy: {accuracy_score(y_test,pred):.4f}\n\n{classification_report(y_test,pred)}"
(ROOT/"reports"/"model_metrics.txt").write_text(report, encoding="utf-8")
print(report)
