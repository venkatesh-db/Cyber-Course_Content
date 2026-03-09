import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Case Study 1: Transaction Risk Analysis
# Scenario: Detecting high-risk transactions based on amount and location.
transactions = [
    {"transaction_id": "T001", "user": "user1", "amount": 5000, "location": "US", "timestamp": datetime.now() - timedelta(minutes=10)},
    {"transaction_id": "T002", "user": "user2", "amount": 20000, "location": "RU", "timestamp": datetime.now() - timedelta(minutes=5)},
    {"transaction_id": "T003", "user": "user3", "amount": 150, "location": "US", "timestamp": datetime.now()},
]

HIGH_RISK_AMOUNT = 10000
HIGH_RISK_LOCATIONS = ["RU", "NG"]

def analyze_transaction_risk(transactions):
    for transaction in transactions:
        if transaction['amount'] > HIGH_RISK_AMOUNT or transaction['location'] in HIGH_RISK_LOCATIONS:
            logging.warning(f"High-risk transaction detected: {transaction}")
        else:
            logging.info(f"Transaction {transaction['transaction_id']} is low risk.")

analyze_transaction_risk(transactions)

# Case Study 2: False-Positive Reduction
# Scenario: Reducing false positives by adding context to alerts.
alerts = [
    {"alert_id": "A001", "user": "user1", "type": "login", "location": "US", "timestamp": datetime.now() - timedelta(minutes=15)},
    {"alert_id": "A002", "user": "user2", "type": "login", "location": "RU", "timestamp": datetime.now() - timedelta(minutes=10)},
    {"alert_id": "A003", "user": "user1", "type": "transaction", "location": "US", "timestamp": datetime.now() - timedelta(minutes=5)},
]

KNOWN_GOOD_LOCATIONS = ["US", "CA"]

def reduce_false_positives(alerts):
    for alert in alerts:
        if alert['location'] in KNOWN_GOOD_LOCATIONS:
            logging.info(f"False positive alert suppressed: {alert}")
        else:
            logging.warning(f"Valid alert: {alert}")

reduce_false_positives(alerts)

# Case Study 3: Incident Triage
# Scenario: Prioritizing incidents based on severity.
incidents = [
    {"incident_id": "I001", "type": "data_exfiltration", "severity": "high", "timestamp": datetime.now() - timedelta(hours=1)},
    {"incident_id": "I002", "type": "phishing", "severity": "medium", "timestamp": datetime.now() - timedelta(hours=2)},
    {"incident_id": "I003", "type": "malware", "severity": "low", "timestamp": datetime.now() - timedelta(hours=3)},
]

SEVERITY_PRIORITY = {"high": 1, "medium": 2, "low": 3}

def triage_incidents(incidents):
    sorted_incidents = sorted(incidents, key=lambda x: SEVERITY_PRIORITY[x['severity']])
    for incident in sorted_incidents:
        logging.info(f"Triage incident: {incident}")

triage_incidents(incidents)