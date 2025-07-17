from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import numpy as np
from sklearn.linear_model import LogisticRegression

app = FastAPI()

# Define request schema
class TestLog(BaseModel):
    rack_id: str
    rpm: float
    temp: float
    slot_health: int

# Train dummy ML model
X = np.array([
    [4000, 60, 50],
    [4200, 65, 60],
    [3500, 75, 30],
    [4800, 45, 90],
    [3000, 85, 20],
    [4400, 55, 80]
])
y = np.array([1, 1, 1, 0, 1, 0])
model = LogisticRegression()
model.fit(X, y)

@app.get("/predict")
def health_check():
    return {"message": "RackWiseAI is running!"}

@app.post("/predict")
def predict_failure(data: TestLog):
    features = np.array([[data.rpm, data.temp, data.slot_health]])
    prediction = model.predict(features)[0]
    score = model.predict_proba(features)[0][1] * 100
    risk = "HIGH" if prediction == 1 else "LOW"

    print("✅ Inside /predict – attempting to write log")

    try:
        with open("predictions.log", "a") as log_file:
            log_file.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                f"rack_id={data.rack_id}, rpm={data.rpm}, temp={data.temp}, "
                f"slot_health={data.slot_health}, score={round(score, 2)}, "
                f"predicted_risk={risk}\n"
            )
        print("✅ Log successfully written!")
    except Exception as e:
        print(f"❌ Logging failed: {e}")

    return {
        "rack_id": data.rack_id,
        "score": round(score, 2),
        "predicted_risk": risk
    }


