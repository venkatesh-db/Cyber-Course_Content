# Placeholder for playbook to notify fraud team

def notify_fraud_team(incident_id, details):
    """
    Notify the fraud team about an incident.

    Args:
        incident_id (str): The ID of the incident.
        details (str): Details about the incident.

    Returns:
        dict: Action result.
    """
    # Simulate notifying the fraud team
    action_result = {
        "action": "notify_fraud_team",
        "incident_id": incident_id,
        "status": "success",
        "message": f"Fraud team notified about incident {incident_id}. Details: {details}"
    }
    print(action_result["message"])
    return action_result

if __name__ == "__main__":
    # Example usage
    sample_incident_id = "INC12345"
    sample_details = "Suspicious login attempts detected."
    result = notify_fraud_team(sample_incident_id, sample_details)
    print("Action Result:", result)