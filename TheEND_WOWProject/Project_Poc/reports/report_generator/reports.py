

import json
from datetime import datetime

def create_report(alert):

    print("Creating report...")

    report = {
        "incident": alert.get("type"),
        "ip": alert.get("ip"),
        "attempts": alert.get("attempts"),
        "timestamp": datetime.now().isoformat()
    }

    print("JSON report will be created...")

    with open("reports/incident_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("File created successfully!")