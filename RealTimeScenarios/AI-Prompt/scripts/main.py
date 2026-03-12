import sys
import os

# Ensure the modules package is discoverable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from modules.log_parser import LogParser
from modules.detection_engine import DetectionEngine
from modules.alert_manager import AlertManager
from modules.incident_response import IncidentResponse

def main():
    print("[INFO] Starting SOC Automation Simulation...")

    # Define log file paths
    log_files = {
        "windows_firewall": os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs/windows_firewall.log"),
        "linux_system": os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs/linux_system.log"),
        "email_logs": os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs/email_logs.log"),
        "malware_activity": os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs/malware_activity.log"),
    }

    # Parse logs
    parser = LogParser()
    parsed_logs = {}
    for log_type, log_path in log_files.items():
        if os.path.exists(log_path):
            print(f"[INFO] Parsing {log_type} logs...")
            parsed_logs[log_type] = parser.parse(log_path)
        else:
            print(f"[WARNING] Log file not found: {log_path}")

    # Apply detection rules
    detection_engine = DetectionEngine()
    alerts = []
    for log_type, df in parsed_logs.items():
        print(f"[INFO] Applying detection rules to {log_type} logs...")
        alerts.extend(detection_engine.apply_rules(log_type, df))

    # Manage alerts
    alert_manager = AlertManager()
    filtered_alerts = alert_manager.filter_alerts(alerts)

    # Generate incident tickets and trigger responses
    incident_response = IncidentResponse()
    for alert in filtered_alerts:
        incident_response.handle_alert(alert)

    print("[INFO] SOC Automation Simulation completed.")

if __name__ == "__main__":
    main()