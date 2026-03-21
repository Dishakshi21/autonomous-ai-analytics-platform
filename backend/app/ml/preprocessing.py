import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_dataset(filepath):

    df = pd.read_csv(filepath)

    # Fill missing values
    df = df.fillna(df.median(numeric_only=True))

    # Encode categorical variables
    df = pd.get_dummies(df)

    # Scale numeric values
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().to_dict()
    }

    return df, summary