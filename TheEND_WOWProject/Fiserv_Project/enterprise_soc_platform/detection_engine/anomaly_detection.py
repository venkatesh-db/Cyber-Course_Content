from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(data, contamination=0.01):
    """
    Detect anomalies in the data using Isolation Forest.

    Args:
        data (list of dict): List of log entries with numerical features.
        contamination (float): Proportion of anomalies in the data.

    Returns:
        list: Anomaly scores for each log entry.
    """
    # Extract numerical features for anomaly detection
    feature_matrix = np.array([
        [entry.get("transaction_amount", 0), entry.get("api_request_rate", 0)]
        for entry in data
    ])

    # Train Isolation Forest
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(feature_matrix)

    # Predict anomaly scores
    scores = model.decision_function(feature_matrix)
    anomalies = model.predict(feature_matrix)

    # Add anomaly scores to log entries
    for i, entry in enumerate(data):
        entry["anomaly_score"] = scores[i]
        entry["is_anomaly"] = anomalies[i] == -1

    return data

if __name__ == "__main__":
    # Example usage
    sample_data = [
        {"transaction_amount": 100, "api_request_rate": 5},
        {"transaction_amount": 10000, "api_request_rate": 50},
        {"transaction_amount": 10, "api_request_rate": 1}
    ]
    results = detect_anomalies(sample_data)
    print("Anomaly detection results:")
    for result in results:
        print(result)