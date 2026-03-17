from incident_manager import create_incident, escalate_incident
from case_tracker import CaseTracker

def test_incident_management():
    # Initialize the case tracker
    tracker = CaseTracker()

    # Sample correlated event
    sample_correlated_event = {
        "incident_type": "Account Takeover",
        "events": [
            {"event_type": "failed_login", "user_id": "user123"},
            {"event_type": "successful_login", "user_id": "user123"}
        ]
    }

    # Test incident creation
    print("Testing Incident Creation...")
    incident = create_incident(sample_correlated_event)
    print("Created Incident:", incident)

    # Test escalation
    print("\nTesting Incident Escalation...")
    escalation_level = escalate_incident(incident)
    print("Escalation Level:", escalation_level)

    # Test case tracking
    print("\nTesting Case Tracking...")
    case_id = tracker.add_case(incident)
    print("Added Case:", tracker.get_case(case_id))
    tracker.update_case_status(case_id, "In Progress")
    print("Updated Case:", tracker.get_case(case_id))

if __name__ == "__main__":
    test_incident_management()