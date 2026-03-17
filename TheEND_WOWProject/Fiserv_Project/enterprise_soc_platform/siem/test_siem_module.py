from alert_generator import generate_alert
from event_correlator import correlate_events_for_siem

def test_siem_module():
    # Sample data for testing
    sample_events = [
        {"event_type": "low_value_transaction", "transaction_id": "123", "ip_address": "192.168.1.1"},
        {"event_type": "low_value_transaction", "transaction_id": "124", "ip_address": "192.168.1.1"},
        {"event_type": "failed_login", "user_id": "user123", "geo_location": "US"},
        {"event_type": "successful_login", "user_id": "user123", "geo_location": "IN"}
    ]

    # Test event correlation
    print("Testing Event Correlation for SIEM...")
    correlated_events = correlate_events_for_siem(sample_events)
    for correlation in correlated_events:
        print(correlation)

    # Test alert generation
    print("\nTesting Alert Generation...")
    for correlated_event in correlated_events:
        alert = generate_alert(correlated_event)
        print(alert)

if __name__ == "__main__":
    test_siem_module()