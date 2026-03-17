from log_ingestion.log_collector import collect_logs
from log_ingestion.parser import parse_logs
from log_ingestion.masker import mask_sensitive_fields as mask_sensitive_data
from log_ingestion.normalizer import normalize_log as normalize_logs
from detection_engine.anomaly_detection import detect_anomalies
from detection_engine.fraud_detection_rules import detect_fraudulent_activity as apply_fraud_rules
from detection_engine.correlation_engine import correlate_events
from siem.alert_generator import generate_alert as generate_alerts
from siem.event_correlator import correlate_events_for_siem as correlate_alerts
from threat_intelligence.ip_reputation import check_ip_reputation
from threat_intelligence.bot_detection import detect_bot_activity as detect_bots
from incident_management.incident_manager import create_incident
from automation.soar_integration import execute_playbook

def orchestrate():
    """
    Orchestrate the flow of data and actions between all modules.
    """
    print("Starting SOC Orchestration...")

    # Step 1: Log Ingestion
    log_directory = "/Users/venkatesh/Cyber-Security Program/TheEND_WOWProject/Fiserv_Project/data_sources/payment_logs"  # Updated to absolute path
    raw_logs = collect_logs(log_directory)
    required_fields = ["transaction_id", "customer_id", "amount"]  # Define required fields
    parsed_logs = parse_logs(raw_logs, required_fields)
    sensitive_fields = ["PAN", "email"]  # Define sensitive fields to mask
    masked_logs = mask_sensitive_data(parsed_logs, sensitive_fields)

    # Step 2: Detection Engine
    normalized_logs = [normalize_logs(log) for log in masked_logs]  # Corrected function name
    # Ensure `normalized_logs` is not empty
    if not normalized_logs:
        print("No valid logs to process.")
        return

    # Ensure numerical features are present for anomaly detection
    for log in normalized_logs:
        log.setdefault("transaction_amount", 0)
        log.setdefault("api_request_rate", 0)

    anomalies = detect_anomalies(normalized_logs)
    fraud_events = [apply_fraud_rules(log) for log in normalized_logs]  # Process each log entry individually
    correlated_events = correlate_events(anomalies + fraud_events)

    # Step 3: SIEM
    alerts = [generate_alerts(event) for event in correlated_events]  # Process each correlated event individually
    correlated_alerts = correlate_alerts(alerts)

    # Step 4: Threat Intelligence
    for alert in correlated_alerts:
        ip_reputation = check_ip_reputation(alert.get("source_ip"))
        bot_detection = detect_bots(alert.get("user_agent"))
        alert.update({"ip_reputation": ip_reputation, "bot_detection": bot_detection})

    # Step 5: Incident Management
    for alert in correlated_alerts:
        incident = create_incident(alert)
        print(f"Incident Created: {incident}")

        # Step 6: Automation (SOAR)
        if alert.get("ip_reputation") == "malicious":
            execute_playbook("block_ip", ip_address=alert.get("source_ip"))
        if alert.get("bot_detection") == "bot_detected":
            execute_playbook("suspend_account", account_id=alert.get("user_id"))
        execute_playbook("notify_fraud_team", incident_id=incident.get("id"), details=incident.get("details"))

    print("SOC Orchestration Completed.")

if __name__ == "__main__":
    orchestrate()