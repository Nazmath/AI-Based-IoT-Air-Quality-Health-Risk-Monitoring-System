from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
rows = []
for _ in range(6000):
    cls = rng.choice(["LOW", "MODERATE", "HIGH", "CRITICAL"], p=[.40,.30,.20,.10])
    if cls == "LOW":
        t,h,g,p = rng.normal(24,2),rng.normal(45,6),rng.normal(60,18),rng.normal(10,4)
    elif cls == "MODERATE":
        t,h,g,p = rng.normal(27,3),rng.normal(55,7),rng.normal(150,30),rng.normal(30,8)
    elif cls == "HIGH":
        t,h,g,p = rng.normal(31,3),rng.normal(65,8),rng.normal(280,45),rng.normal(65,14)
    else:
        t,h,g,p = rng.normal(35,4),rng.normal(75,9),rng.normal(420,55),rng.normal(105,20)
    rows.append([t,h,max(g,0),max(p,0),cls])

root = Path(__file__).resolve().parents[1]
pd.DataFrame(rows, columns=["temperature_c","humidity_pct","gas_index","pm25_ugm3","risk"]).to_csv(root/"data"/"air_quality_dataset.csv", index=False)
print("Generated dataset")
