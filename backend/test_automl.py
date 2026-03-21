import pandas as pd
from app.ml.preprocessing import preprocess_dataset
from app.ml.automl import train_automl_model

# run preprocessing first
cleaned_df, summary = preprocess_dataset("app/uploads/sample_data.csv")

# run automl on cleaned data
result = train_automl_model(cleaned_df, "Salary")

print(result)