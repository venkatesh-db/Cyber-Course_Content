class AlertManager:
    def filter_alerts(self, alerts):
        """Filter alerts to reduce noise."""
        # Example: Only keep alerts with severity High or Critical
        return [alert for alert in alerts if alert["severity"] in ["High", "Critical"]]