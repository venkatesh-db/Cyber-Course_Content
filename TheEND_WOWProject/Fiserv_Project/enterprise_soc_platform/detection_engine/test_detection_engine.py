from anomaly_detection import detect_anomalies
from fraud_detection_rules import detect_fraudulent_activity
from correlation_engine import correlate_events

def test_detection_engine():
    # Sample data for testing
    sample_logs = [
        {"transaction_id": "1", "transaction_amount": 100, "api_request_rate": 5},
        {"transaction_id": "2", "transaction_amount": 15000, "api_request_rate": 50},
        {"transaction_id": "3", "transaction_amount": 10, "api_request_rate": 1},
        {"event_type": "failed_login", "user_id": "user123", "geo_location": "US"},
        {"event_type": "successful_login", "user_id": "user123", "geo_location": "IN"}
    ]

    # Test anomaly detection
    print("Testing Anomaly Detection...")
    anomaly_results = detect_anomalies(sample_logs)
    for result in anomaly_results:
        print(result)

    # Test fraud detection rules
    print("\nTesting Fraud Detection Rules...")
    for log in sample_logs:
        fraud_result = detect_fraudulent_activity(log)
        print(fraud_result)

    # Test event correlation
    print("\nTesting Event Correlation...")
    correlation_results = correlate_events(sample_logs)
    for correlation in correlation_results:
        print(correlation)

if __name__ == "__main__":
    test_detection_engine()