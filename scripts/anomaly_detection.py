import pandas as pd
from sklearn.ensemble import IsolationForest
from loguru import logger

def detect_anomalies(df: pd.DataFrame):
    if df.empty:
        logger.warning("No data for anomaly detection")
        return []

    # Use only numerical features for ML
    features = pd.get_dummies(df[["pid", "host", "process", "action", "status"]])
    model = IsolationForest(contamination=0.1, random_state=42)
    preds = model.fit_predict(features)

    df["anomaly"] = preds
    anomalies = df[df["anomaly"] == -1]
    return anomalies.to_dict(orient="records")
