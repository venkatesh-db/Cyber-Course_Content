import logging
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Module 12: ML Models That Actually Work in Finance
# Case Study: Isolation Forest for Transaction Behavior Analysis

def isolation_forest_analysis(transactions):
    data = np.array([[t['transaction_id'], t['amount']] for t in transactions])

    # Train Isolation Forest
    clf = IsolationForest(contamination=0.2, random_state=42)
    clf.fit(data)

    # Predict anomalies
    predictions = clf.predict(data)
    for i, prediction in enumerate(predictions):
        if prediction == -1:
            logging.warning(f"Anomalous transaction detected: {transactions[i]}")
        else:
            logging.info(f"Normal transaction: {transactions[i]}")

# Why Deep Learning is Dangerous Here
# Deep learning models often require large datasets and can overfit to noise in financial data.
# They may lack transparency, making them unsuitable for audit and compliance requirements.

# Model Explainability: Audit Survival
# Explainability is critical in finance to ensure models are auditable and compliant.
# Isolation Forest provides feature importance and anomaly scores for explainability.

def explain_model(clf, transactions):
    scores = clf.decision_function(np.array([[t['transaction_id'], t['amount']] for t in transactions]))
    for i, score in enumerate(scores):
        logging.info(f"Transaction: {transactions[i]}, Anomaly Score: {score}")

# Example Transactions
def fiserv_use_case():
    transactions = [
        {"transaction_id": 1, "amount": 100, "timestamp": datetime.now() - timedelta(minutes=10)},
        {"transaction_id": 2, "amount": 150, "timestamp": datetime.now() - timedelta(minutes=5)},
        {"transaction_id": 3, "amount": 10000, "timestamp": datetime.now()},
        {"transaction_id": 4, "amount": 120, "timestamp": datetime.now() - timedelta(minutes=15)},
        {"transaction_id": 5, "amount": 20000, "timestamp": datetime.now() - timedelta(minutes=20)},
    ]

    isolation_forest_analysis(transactions)

    # Train Isolation Forest for explainability
    clf = IsolationForest(contamination=0.2, random_state=42)
    clf.fit(np.array([[t['transaction_id'], t['amount']] for t in transactions]))
    explain_model(clf, transactions)

if __name__ == "__main__":
    fiserv_use_case()