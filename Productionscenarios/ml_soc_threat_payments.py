# source venv/bin/activate && pip install numpy

import logging
import numpy as np
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Module 9: ML for SOC
# Case Study: Anomaly Detection with Isolation Forest

data = np.array([
    [1, 100],  # Normal transaction
    [2, 150],  # Normal transaction
    [3, 10000],  # Anomalous transaction
    [4, 120],  # Normal transaction
    [5, 20000],  # Anomalous transaction
])

# Train Isolation Forest
clf = IsolationForest(contamination=0.2, random_state=42)
clf.fit(data)

# Predict anomalies
predictions = clf.predict(data)
for i, prediction in enumerate(predictions):
    if prediction == -1:
        logging.warning(f"Anomalous transaction detected: {data[i]}")
    else:
        logging.info(f"Normal transaction: {data[i]}")

# Module 10: Threat Intelligence Enrichment
# Case Study: Enriching Indicators with Threat Scoring
indicators = [
    {"type": "ip", "value": "192.168.1.1", "behavior": "scanning"},
    {"type": "hash", "value": "abcd1234", "behavior": "malware"},
    {"type": "domain", "value": "example.com", "behavior": "phishing"},
]

ATTACK_MAPPING = {
    "scanning": "Reconnaissance",
    "malware": "Execution",
    "phishing": "Credential Access",
}

THREAT_SCORES = {
    "Reconnaissance": 30,
    "Execution": 70,
    "Credential Access": 90,
}

def enrich_indicators(indicators):
    for indicator in indicators:
        behavior = indicator['behavior']
        attack_phase = ATTACK_MAPPING.get(behavior, "Unknown")
        threat_score = THREAT_SCORES.get(attack_phase, 0)
        logging.info(f"Indicator: {indicator['value']}, Attack Phase: {attack_phase}, Threat Score: {threat_score}")

enrich_indicators(indicators)

# Module 11: Payments-Focused Feature Engineering
# Case Study: Engineering Features for Payments
transactions = [
    {"transaction_id": "T001", "user": "user1", "amount": 500, "location": "US", "timestamp": datetime.now() - timedelta(minutes=10)},
    {"transaction_id": "T002", "user": "user1", "amount": 1000, "location": "US", "timestamp": datetime.now() - timedelta(minutes=5)},
    {"transaction_id": "T003", "user": "user1", "amount": 200, "location": "CA", "timestamp": datetime.now()},
]

# Feature: Transaction Velocity
def calculate_transaction_velocity(transactions):
    velocities = []
    for i in range(1, len(transactions)):
        time_diff = (transactions[i]['timestamp'] - transactions[i - 1]['timestamp']).total_seconds() / 60  # in minutes
        velocities.append(1 / time_diff if time_diff > 0 else 0)
    return velocities

# Feature: Amount Deviation
def calculate_amount_deviation(transactions):
    amounts = [t['amount'] for t in transactions]
    mean_amount = np.mean(amounts)
    deviations = [abs(t['amount'] - mean_amount) for t in transactions]
    return deviations

# Feature: Geo Mismatch
def detect_geo_mismatch(transactions):
    base_location = transactions[0]['location']
    mismatches = [t for t in transactions if t['location'] != base_location]
    return mismatches

# Feature: API Usage Frequency
def calculate_api_usage_frequency(transactions):
    time_window = timedelta(minutes=15)
    recent_transactions = [t for t in transactions if t['timestamp'] > datetime.now() - time_window]
    return len(recent_transactions)

# Feature: Privileged Access Timing
def detect_privileged_access_timing(transactions):
    privileged_hours = range(0, 6)  # Midnight to 6 AM
    privileged_access = [t for t in transactions if t['timestamp'].hour in privileged_hours]
    return privileged_access

# Calculate features
logging.info(f"Transaction Velocity: {calculate_transaction_velocity(transactions)}")
logging.info(f"Amount Deviation: {calculate_amount_deviation(transactions)}")
logging.info(f"Geo Mismatches: {detect_geo_mismatch(transactions)}")
logging.info(f"API Usage Frequency: {calculate_api_usage_frequency(transactions)}")
logging.info(f"Privileged Access Timing: {detect_privileged_access_timing(transactions)}")