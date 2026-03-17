# Placeholder for event correlation logic in SIEM

def correlate_events_for_siem(events):
    """
    Correlate events to detect potential incidents for SIEM.

    Args:
        events (list of dict): List of raw events.

    Returns:
        list: Correlated events with incident details.
    """
    correlated_events = []

    # Example correlation: Card Testing Attack
    for event in events:
        if event.get("event_type") == "low_value_transaction":
            for other_event in events:
                if (
                    other_event.get("event_type") == "low_value_transaction"
                    and other_event.get("ip_address") == event.get("ip_address")
                    and other_event.get("transaction_id") != event.get("transaction_id")
                ):
                    correlated_events.append({
                        "incident_type": "Card Testing Attack",
                        "events": [event, other_event]
                    })

    return correlated_events

if __name__ == "__main__":
    # Example usage
    sample_events = [
        {"event_type": "low_value_transaction", "transaction_id": "123", "ip_address": "192.168.1.1"},
        {"event_type": "low_value_transaction", "transaction_id": "124", "ip_address": "192.168.1.1"}
    ]
    results = correlate_events_for_siem(sample_events)
    print("Correlated events for SIEM:", results)