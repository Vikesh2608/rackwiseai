# 🧠 RackWiseAI - Predictive Failure Detection (Dockerized)

RackWiseAI is an ML-powered FastAPI application designed to predict hardware failure risk in server racks.  
It runs inside a Docker container and exposes REST APIs for real-time inference and logging.

---

## 🚀 Features

- ✅ FastAPI backend with OpenAPI docs
- ✅ Logistic Regression model (`scikit-learn`)
- ✅ Real-time predictions via `/predict`
- ✅ Auto logs predictions to `predictions.log`
- ✅ Dockerized for portable deployment
- ✅ Deployed on AWS EC2

---

## 📦 Tech Stack

- Python 3.12
- FastAPI + Uvicorn
- scikit-learn
- Docker

---

## 🧪 Example Request

```bash
curl -X POST "http://<your-public-ip>:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"rack_id": "RACK-17", "rpm": 4300, "temp": 67.5, "slot_health": 65}'

```
**Response:**
```json
{
  "rack_id": "RACK-17",
  "score": 51.7,
  "predicted_risk": "HIGH"
}
```

