# Placeholder for fraud detection rules

def detect_fraudulent_activity(log_entry):
    """
    Detect fraudulent activity based on predefined rules.

    Args:
        log_entry (dict): A single log entry.

    Returns:
        dict: The log entry with an added fraud flag and reason if applicable.
    """
    fraud_detected = False
    fraud_reason = ""

    # Rule 1: Unusually high transaction amount
    if log_entry.get("transaction_amount", 0) > 10000:
        fraud_detected = True
        fraud_reason = "High transaction amount"

    # Rule 2: Multiple failed login attempts
    if log_entry.get("failed_login_attempts", 0) > 5:
        fraud_detected = True
        fraud_reason = "Multiple failed login attempts"

    # Rule 3: Suspicious geolocation
    if log_entry.get("geo_location", "") in ["suspicious_country_1", "suspicious_country_2"]:
        fraud_detected = True
        fraud_reason = "Suspicious geolocation"

    log_entry["fraud_detected"] = fraud_detected
    log_entry["fraud_reason"] = fraud_reason
    return log_entry

if __name__ == "__main__":
    # Example usage
    sample_log = {
        "transaction_amount": 15000,
        "failed_login_attempts": 2,
        "geo_location": "suspicious_country_1"
    }
    result = detect_fraudulent_activity(sample_log)
    print("Fraud detection result:", result)