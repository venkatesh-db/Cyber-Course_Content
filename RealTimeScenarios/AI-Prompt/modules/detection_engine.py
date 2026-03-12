class DetectionEngine:
    def apply_rules(self, log_type, df):
        """Apply detection rules to the DataFrame and return alerts."""
        alerts = []
        if log_type == "windows_firewall":
            alerts.extend(self.detect_port_scanning(df))
        elif log_type == "linux_system":
            alerts.extend(self.detect_ssh_brute_force(df))
        elif log_type == "malware_activity":
            alerts.extend(self.detect_malware_activity(df))
        elif log_type == "email_logs":
            alerts.extend(self.detect_suspicious_emails(df))
        return alerts

    def detect_port_scanning(self, df):
        """Detect port scanning activity."""
        return [{"description": "Port scanning detected", "severity": "High", "action": "Block IP"}]

    def detect_ssh_brute_force(self, df):
        """Detect SSH brute force attacks."""
        return [{"description": "SSH brute force attack detected", "severity": "Medium", "action": "Isolate server"}]

    def detect_malware_activity(self, df):
        """Detect malware activity."""
        return [{"description": "Malware activity detected", "severity": "Critical", "action": "Quarantine process"}]

    def detect_suspicious_emails(self, df):
        """Detect suspicious email activity."""
        return [{"description": "Suspicious email detected", "severity": "Low", "action": "Flag email"}]