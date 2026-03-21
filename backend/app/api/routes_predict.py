from fastapi import APIRouter
import joblib
import pandas as pd

router = APIRouter()

# Load saved model
model = joblib.load("app/models_trained/best_model.pkl")


@router.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return {
        "prediction": float(prediction[0])
    }