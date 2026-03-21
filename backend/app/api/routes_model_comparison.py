from fastapi import APIRouter
import json
import os

router = APIRouter()

MODEL_RESULTS_FILE = "app/models_trained/model_scores.json"


@router.get("/model-comparison")
def model_comparison():

    if not os.path.exists(MODEL_RESULTS_FILE):
        return {"error": "No model training results found"}

    with open(MODEL_RESULTS_FILE, "r") as f:
        scores = json.load(f)

    return {
        "model_comparison": scores
    }