import logging
import numpy as np
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='threat_logs.log', filemode='w')

# Generate synthetic transaction data for 10 months
def generate_transaction_data():
    transactions = []
    start_date = datetime.now() - timedelta(days=300)  # Start 10 months ago
    for i in range(1, 10001):  # 10,000 transactions
        transaction = {
            "transaction_id": i,
            "amount": random.randint(10, 50000),
            "timestamp": start_date + timedelta(minutes=random.randint(0, 300 * 24 * 60)),
            "location": random.choice(["US", "CA", "UK", "IN", "DE"]),
            "cyber_signal": random.choice(["phishing", "malware", "scanning", "none"]),
        }
        transactions.append(transaction)
    return transactions

# Build anomaly detection on transaction streams
def detect_anomalies(transactions):
    data = np.array([[t['transaction_id'], t['amount']] for t in transactions])
    clf = IsolationForest(contamination=0.1, random_state=42)
    clf.fit(data)
    predictions = clf.predict(data)

    for i, prediction in enumerate(predictions):
        if prediction == -1:
            logging.warning(f"Anomalous transaction detected: {transactions[i]}")
        else:
            logging.info(f"Normal transaction: {transactions[i]}")

# Correlate cyber + payment signals
def correlate_signals(transactions):
    for transaction in transactions:
        if transaction['cyber_signal'] != "none":
            logging.warning(f"Cyber signal detected: {transaction['cyber_signal']} in transaction {transaction}")

# Generate explainable risk scores
def generate_risk_scores(transactions):
    RISK_FACTORS = {
        "phishing": 50,
        "malware": 70,
        "scanning": 30,
        "none": 0,
    }

    for transaction in transactions:
        cyber_risk = RISK_FACTORS[transaction['cyber_signal']]
        amount_risk = min(transaction['amount'] / 1000, 50)  # Cap amount risk at 50
        total_risk = cyber_risk + amount_risk
        logging.info(f"Transaction: {transaction}, Risk Score: {total_risk}")

if __name__ == "__main__":
    transactions = generate_transaction_data()
    detect_anomalies(transactions)
    correlate_signals(transactions)
    generate_risk_scores(transactions)