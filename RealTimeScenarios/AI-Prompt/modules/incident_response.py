class IncidentResponse:
    def handle_alert(self, alert):
        """Handle the alert by creating an incident ticket and triggering a response."""
        print(f"[ALERT] {alert['description']}")
        print(f"Severity: {alert['severity']}")
        print(f"Recommended Action: {alert['action']}")
        # Example: Create incident ticket and trigger response
        self.create_incident_ticket(alert)
        self.trigger_response(alert)

    def create_incident_ticket(self, alert):
        """Create an incident ticket."""
        print("[INFO] Incident ticket created.")

    def trigger_response(self, alert):
        """Trigger an automated response based on the alert."""
        print(f"[INFO] Triggering response: {alert['action']}")