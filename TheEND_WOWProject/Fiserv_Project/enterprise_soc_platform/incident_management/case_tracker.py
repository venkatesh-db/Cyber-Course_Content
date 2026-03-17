from datetime import datetime

class CaseTracker:
    def __init__(self):
        self.cases = {}

    def add_case(self, incident):
        """
        Add a new case to the tracker.

        Args:
            incident (dict): The incident to track.

        Returns:
            str: Case ID.
        """
        case_id = incident.get("incident_id")
        self.cases[case_id] = {
            "incident": incident,
            "status": "Open",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        return case_id

    def update_case_status(self, case_id, status):
        """
        Update the status of a case.

        Args:
            case_id (str): The ID of the case to update.
            status (str): The new status of the case.

        Returns:
            bool: True if the case was updated, False otherwise.
        """
        if case_id in self.cases:
            self.cases[case_id]["status"] = status
            self.cases[case_id]["updated_at"] = datetime.utcnow().isoformat()
            return True
        return False

    def get_case(self, case_id):
        """
        Retrieve a case by its ID.

        Args:
            case_id (str): The ID of the case to retrieve.

        Returns:
            dict: The case details, or None if not found.
        """
        return self.cases.get(case_id)

if __name__ == "__main__":
    # Example usage
    tracker = CaseTracker()
    sample_incident = {
        "incident_id": "12345",
        "incident_type": "Account Takeover",
        "severity": "high",
        "affected_users": ["user123"],
        "timeline_of_events": []
    }
    case_id = tracker.add_case(sample_incident)
    print("Added Case:", tracker.get_case(case_id))
    tracker.update_case_status(case_id, "In Progress")
    print("Updated Case:", tracker.get_case(case_id))