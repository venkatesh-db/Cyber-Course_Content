'''
Linux Logs
     ↓
Splunk Detection
     ↓
Webhook → Python SOAR
     ↓
Threat Enrichment (AbuseIPDB)
     ↓
Decision Engine
     ↓
iptables Block
     ↓
Email SOC
'''


import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Threat intelligence API configurations
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "VALID_VIRUSTOTAL_API_KEY")  # Replace with your valid VirusTotal API key
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY", "VALID_ABUSEIPDB_API_KEY")  # Replace with your valid AbuseIPDB API key

# SOC notification configurations
SOC_EMAIL = "soc_team@example.com"
SMTP_SERVER = "smtp.gmail.com"  # Example: Gmail SMTP server
SMTP_PORT = 587  # TLS port for Gmail
SMTP_USER = "your_email@gmail.com"  # Replace with your email address
SMTP_PASSWORD = "your_app_password"  # Replace with your Gmail App Password

# Function to enrich threat data using VirusTotal
def enrich_with_virustotal(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"VirusTotal API error: {response.status_code} - {response.text}")
        return None

# Function to enrich threat data using AbuseIPDB
def enrich_with_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"AbuseIPDB API error: {response.status_code} - {response.text}")
        return None

# Function to block IP using pfctl (macOS-compatible)
def block_ip(ip):
    try:
        # Ensure the blocklist table exists
        subprocess.run(["sudo", "pfctl", "-t", "blocklist", "-T", "show"], check=True)
        # Add the IP to the block table
        subprocess.run(["sudo", "pfctl", "-t", "blocklist", "-T", "add", ip], check=True)
        logging.info(f"Blocked IP: {ip}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to block IP {ip}: {e}")

# Function to notify SOC team
def notify_soc(threat_data):
    try:
        subject = "[ALERT] Threat Detected and Blocked"
        body = json.dumps(threat_data, indent=4)

        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = SOC_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, SOC_EMAIL, msg.as_string())

        logging.info("SOC team notified.")
    except Exception as e:
        logging.error(f"Failed to notify SOC team: {e}")

# Main function to process Splunk alert data
def process_splunk_alert(alert_data):
    try:
        logging.info("Processing Splunk alert...")
        
        # Parse alert data
        alert = json.loads(alert_data)
        suspicious_ip = alert.get("ip")
        if not suspicious_ip:
            logging.error("No IP address found in alert data.")
            return

        # Enrich threat data
        vt_data = enrich_with_virustotal(suspicious_ip)
        abuseipdb_data = enrich_with_abuseipdb(suspicious_ip)

        # Combine enrichment data
        threat_data = {
            "ip": suspicious_ip,
            "virustotal": vt_data,
            "abuseipdb": abuseipdb_data
        }

        # Take automated action
        block_ip(suspicious_ip)

        # Notify SOC team
        notify_soc(threat_data)

    except Exception as e:
        logging.error(f"Error processing Splunk alert: {e}")

# Example usage
if __name__ == "__main__":
    # Simulated Splunk alert data
    sample_alert = json.dumps({"ip": "192.168.1.100"})
    process_splunk_alert(sample_alert)