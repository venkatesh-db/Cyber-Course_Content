from collections import defaultdict
from datetime import datetime, timedelta

# Sample log data (replace with actual log file parsing)
logs = [
    {"ip": "192.168.1.1", "status": "failed", "timestamp": "2026-02-25 10:00:00"},
    {"ip": "192.168.1.1", "status": "failed", "timestamp": "2026-02-25 10:01:00"},
    {"ip": "192.168.1.1", "status": "failed", "timestamp": "2026-02-25 10:02:00"},
    {"ip": "192.168.1.2", "status": "success", "timestamp": "2026-02-25 10:03:00"},
    {"ip": "192.168.1.3", "status": "failed", "timestamp": "2026-02-25 10:04:00"},
    {"ip": "192.168.1.3", "status": "failed", "timestamp": "2026-02-25 10:05:00"},
]

# Parameters
time_window = timedelta(minutes=5)  # Time window to detect attacks
failed_attempts_threshold = 3  # Number of failed attempts to consider an attack

# Parse logs and detect failed login attacks
def detect_failed_login_attacks(logs):
    failed_attempts = defaultdict(list)
    attack_ips = set()

    for log in logs:
        if log["status"] == "failed":
            ip = log["ip"]
            timestamp = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S")
            failed_attempts[ip].append(timestamp)

            # Check if the number of failed attempts exceeds the threshold within the time window
            recent_attempts = [
                t for t in failed_attempts[ip] if t >= timestamp - time_window
            ]
            if len(recent_attempts) >= failed_attempts_threshold:
                attack_ips.add(ip)

    return attack_ips

# Detect attacks
attackers = detect_failed_login_attacks(logs)
if attackers:
    print("Failed login attack detected from the following IPs:")
    for ip in attackers:
        print(ip)
else:
    print("No failed login attacks detected.")