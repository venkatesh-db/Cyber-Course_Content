import uuid

def generate_alert(correlated_event):
    """
    Generate an alert based on a correlated event.

    Args:
        correlated_event (dict): A correlated event containing incident details.

    Returns:
        dict: An alert object with severity, confidence score, and other details.
    """
    alert = {
        "alert_id": str(uuid.uuid4()),
        "severity": "high" if correlated_event.get("incident_type") == "Account Takeover" else "medium",
        "incident_type": correlated_event.get("incident_type", "Unknown"),
        "confidence_score": 0.9 if correlated_event.get("incident_type") == "Account Takeover" else 0.7,
        "correlated_events": correlated_event.get("events", [])
    }
    return alert

if __name__ == "__main__":
    # Example usage
    sample_correlated_event = {
        "incident_type": "Account Takeover",
        "events": [
            {"event_type": "failed_login", "user_id": "user123"},
            {"event_type": "successful_login", "user_id": "user123"}
        ]
    }
    alert = generate_alert(sample_correlated_event)
    print("Generated alert:", alert)