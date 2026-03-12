import pandas as pd
import re
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Log file path
LOG_FILE = "/Users/venkatesh/Cyber-Security Program/RealTimeScenarios/ServerLogAnalysis/server_logs.txt"

# Function to parse logs and convert to DataFrame
def parse_logs_to_dataframe(log_file):
    log_entries = []

    try:
        with open(log_file, "r") as file:
            for line in file:
                # Example log parsing logic
                match = re.match(r"(\w+ \d+ \d+:\d+:\d+) (\w+): (.+)", line)
                if match:
                    timestamp, source, message = match.groups()
                    log_entries.append({"timestamp": timestamp, "source": source, "message": message})
    except FileNotFoundError:
        print(f"[ERROR] Log file {log_file} not found.")

    return pd.DataFrame(log_entries)

# Function to run detection rules
def run_detection_rules(df):
    alerts = []

    # Rule 1: Detect suspicious shared memory
    shared_memory_alerts = df[df['message'].str.contains("suspicious shared memory", na=False)]
    if not shared_memory_alerts.empty:
        alerts.append("Suspicious shared memory detected.")

    # Rule 2: Detect unusual outbound connections
    outbound_alerts = df[df['message'].str.contains("unusual outbound connection", na=False)]
    if not outbound_alerts.empty:
        alerts.append("Unusual outbound connections detected.")

    # Rule 3: Detect unknown processes
    unknown_process_alerts = df[df['message'].str.contains("unknown process", na=False)]
    if not unknown_process_alerts.empty:
        alerts.append("Unknown processes detected.")

    return alerts

# Function to handle detected attacks
def handle_detected_attacks(alerts):
    if alerts:
        print("[ALERT] Attack detected!")
        for alert in alerts:
            print(f"  - {alert}")

        # Production-grade incident ticket creation
        incident_details = {
            "incident_id": f"INC-{pd.Timestamp.now().strftime('%Y%m%d%H%M%S')}",
            "timestamp": pd.Timestamp.now().isoformat(),
            "alerts": alerts,
            "status": "Open",
            "priority": "High",
            "assigned_team": "SOC Team",
            "description": "Automated detection of suspicious activity. Immediate action required.",
        }

        ticket_file = "incident_ticket.json"
        with open(ticket_file, "w") as ticket:
            import json
            json.dump(incident_details, ticket, indent=4)
        print(f"Incident ticket created: {ticket_file}")
        print(json.dumps(incident_details, indent=4))

        # Production-grade automated response
        print("Triggering automated response...")

        # Example: Blocking suspicious IPs using pfctl (macOS compatible)
        try:
            block_command = ["sudo", "pfctl", "-t", "blocklist", "-T", "add", "192.168.1.1"]
            subprocess.run(block_command, check=True)
            print("- Suspicious IP blocked successfully using pfctl.")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to block IP: {e}")

        # Example: Sending email notification with Ethereal Email (demo credentials)
        try:
            sender_email = "ethereal_user@ethereal.email"
            receiver_email = "soc_team@example.com"
            password = "ethereal_password"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "[ALERT] Security Incident Detected"

            body = f"Incident Details:\n{json.dumps(incident_details, indent=4)}"
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP("smtp.ethereal.email", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

            print("- SOC team notified via email.")
        except Exception as e:
            print(f"[ERROR] Failed to send email notification: {e}")

        # Example: Logging system scan action instead of ClamAV
        try:
            print("- Logging system scan action (ClamAV not used on macOS).")
        except Exception as e:
            print(f"[ERROR] Failed to log system scan action: {e}")

        print("Automated response completed successfully.")
    else:
        print("No attacks detected.")

# Main function
def main():
    print("Parsing logs and running detection pipeline...")

    # Parse logs to DataFrame
    df = parse_logs_to_dataframe(LOG_FILE)

    if df.empty:
        print("No logs to analyze.")
        return

    # Run detection rules
    alerts = run_detection_rules(df)

    # Handle detected attacks
    handle_detected_attacks(alerts)

if __name__ == "__main__":
    main()