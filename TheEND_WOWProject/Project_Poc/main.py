


from scripts.log_collector import load_logs
from scripts.deetection_engine import detection_brutforce
from scripts.containment import block
from reports.report_generator import reports




logs= load_logs()
alerts=detection_brutforce(logs)

for alert in alerts:
    print(f"Alert: {alert}")
    block(alert["ip"])
    reports.create_report(alert)
    
