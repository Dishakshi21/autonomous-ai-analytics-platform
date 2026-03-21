import pandas as pd
import numpy as np
import joblib
import json

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error


def train_automl_model(df, target_column):

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    results = {}
    trained_models = {}

    # Detect problem type
    if y.nunique() <= 10:
        problem_type = "classification"

        models = {
            "LogisticRegression": LogisticRegression(max_iter=1000),
            "RandomForestClassifier": RandomForestClassifier()
        }

        for name, model in models.items():
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

            acc = accuracy_score(y_test, preds)
            results[name] = acc
            trained_models[name] = model

        best_model_name = max(results, key=results.get)

    else:
        problem_type = "regression"

        models = {
            "LinearRegression": LinearRegression(),
            "RandomForestRegressor": RandomForestRegressor()
        }

        for name, model in models.items():
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

            rmse = np.sqrt(mean_squared_error(y_test, preds))
            results[name] = rmse
            trained_models[name] = model

        best_model_name = min(results, key=results.get)

    best_model = trained_models[best_model_name]

    # Save best model
    joblib.dump(best_model, "app/models_trained/best_model.pkl")

    # Save model scores for dashboard
    with open("app/models_trained/model_scores.json", "w") as f:
        json.dump(results, f)

    # Explainable AI (Feature Importance)
    feature_importance = {}

    if hasattr(best_model, "feature_importances_"):
        importances = best_model.feature_importances_
        feature_importance = dict(zip(X.columns, importances))

    return {
        "problem_type": problem_type,
        "model_scores": results,
        "best_model": best_model_name,
        "feature_importance": feature_importance
    }