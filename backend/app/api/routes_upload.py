from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_dataset

router = APIRouter()

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    return save_dataset(file)
import joblib

@router.get("/feature-importance")
def feature_importance():

    model = joblib.load("app/models_trained/best_model.pkl")

    if hasattr(model, "feature_importances_"):

        importance = model.feature_importances_
        features = model.feature_names_in_

        result = dict(zip(features, importance))

        return {
            "feature_importance": result
        }

    else:
        return {
            "message": "Feature importance not available for this model"
        }