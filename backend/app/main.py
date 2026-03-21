from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from .database import engine

from app.api.routes_upload import router as upload_router
from app.api.routes_predict import router as predict_router
from app.api.routes_model_comparison import router as comparison_router

app = FastAPI()

# Allow React frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"message": "Database Connected Successfully"}
    except Exception as e:
        return {"error": str(e)}


# Upload dataset API
app.include_router(upload_router)

# Prediction API
app.include_router(predict_router)

# Model comparison API
app.include_router(comparison_router)