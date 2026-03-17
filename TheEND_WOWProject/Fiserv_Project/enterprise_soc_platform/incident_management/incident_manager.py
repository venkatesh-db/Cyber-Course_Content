import uuid

def create_incident(correlated_event):
    """
    Create an incident based on a correlated event.

    Args:
        correlated_event (dict): A correlated event containing incident details.

    Returns:
        dict: An incident object with details.
    """
    incident = {
        "incident_id": str(uuid.uuid4()),
        "incident_type": correlated_event.get("incident_type", "Unknown"),
        "severity": "high" if correlated_event.get("incident_type") == "Account Takeover" else "medium",
        "affected_users": [event.get("user_id") for event in correlated_event.get("events", []) if event.get("user_id")],
        "timeline_of_events": correlated_event.get("events", [])
    }
    return incident

def escalate_incident(incident):
    """
    Escalate an incident based on its severity.

    Args:
        incident (dict): The incident to escalate.

    Returns:
        str: Escalation level.
    """
    if incident.get("severity") == "high":
        return "SOC Level 2"
    else:
        return "SOC Level 1"

if __name__ == "__main__":
    # Example usage
    sample_correlated_event = {
        "incident_type": "Account Takeover",
        "events": [
            {"event_type": "failed_login", "user_id": "user123"},
            {"event_type": "successful_login", "user_id": "user123"}
        ]
    }
    incident = create_incident(sample_correlated_event)
    print("Created Incident:", incident)
    escalation_level = escalate_incident(incident)
    print("Escalation Level:", escalation_level)