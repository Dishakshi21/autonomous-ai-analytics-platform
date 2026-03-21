import os
import pandas as pd
from datetime import datetime

from app.ml.preprocessing import preprocess_dataset
from app.ml.automl import train_automl_model   # NEW IMPORT

UPLOAD_DIR = "app/uploads"


def save_dataset(file):

    # Create upload folder if not exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Read dataset
    df = pd.read_csv(file_path)

    # Run preprocessing pipeline
    cleaned_df, summary = preprocess_dataset(file_path)

    # Run AutoML model training
    model_result = train_automl_model(cleaned_df, "Salary")

    return {
        "filename": file.filename,
        "original_rows": len(df),
        "cleaned_rows": summary["rows"],
        "columns": summary["columns"],
        "missing_values": summary["missing_values"],
        "automl_result": model_result
    }