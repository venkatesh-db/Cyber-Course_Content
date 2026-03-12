import re
from collections import defaultdict
from datetime import datetime, timedelta

# Simulated firewall log file
LOG_FILE = "/Users/venkatesh/Cyber-Security Program/RealTimeScenarios/Firewall/firewall_logs.txt"

# Threshold for triggering an alert
CONNECTION_THRESHOLD = 50
TIME_WINDOW = timedelta(minutes=1)

# Function to parse log lines
def parse_log_line(line):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) DROP TCP (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+) (\d+) (\d+)"
    match = re.match(pattern, line)
    if match:
        timestamp = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
        src_ip = match.group(2)
        dest_ip = match.group(3)
        dest_port = int(match.group(4))
        src_port = int(match.group(5))
        return timestamp, src_ip, dest_ip, dest_port, src_port
    return None

# Function to detect suspicious activity
def detect_port_scanning(log_file):
    connection_attempts = defaultdict(list)
    suspicious_ips = set()

    with open(log_file, "r") as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                timestamp, src_ip, _, _, _ = parsed
                connection_attempts[src_ip].append(timestamp)

    # Analyze connection attempts
    for ip, timestamps in connection_attempts.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            window_start = timestamps[i]
            window_end = window_start + TIME_WINDOW
            count = sum(1 for t in timestamps if window_start <= t < window_end)
            if count > CONNECTION_THRESHOLD:
                suspicious_ips.add(ip)
                break

    return suspicious_ips

# Function to simulate automated response
def automated_response(suspicious_ips):
    for ip in suspicious_ips:
        print(f"Blocking IP: {ip}")
        print(f"Creating incident ticket for IP: {ip}")
        print(f"Notifying SOC team about IP: {ip}")

# Main function
def main():
    print("Analyzing firewall logs...")
    suspicious_ips = detect_port_scanning(LOG_FILE)

    if suspicious_ips:
        print(f"Suspicious IPs detected: {suspicious_ips}")
        automated_response(suspicious_ips)
    else:
        print("No suspicious activity detected.")

if __name__ == "__main__":
    main()