# Case Study 1: Failed Logins
# Scenario: Detecting brute-force attacks based on failed login attempts.
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated login attempts
login_attempts = [
    {"user": "admin", "ip": "192.168.1.1", "timestamp": datetime.now() - timedelta(minutes=5)},
    {"user": "admin", "ip": "192.168.1.1", "timestamp": datetime.now() - timedelta(minutes=4)},
    {"user": "admin", "ip": "192.168.1.1", "timestamp": datetime.now() - timedelta(minutes=3)},
    {"user": "admin", "ip": "192.168.1.1", "timestamp": datetime.now() - timedelta(minutes=2)},
    {"user": "admin", "ip": "192.168.1.1", "timestamp": datetime.now() - timedelta(minutes=1)},
]

# Threshold for failed logins
THRESHOLD = 5
TIME_WINDOW = timedelta(minutes=10)

def detect_brute_force(attempts):
    recent_attempts = [a for a in attempts if a['timestamp'] > datetime.now() - TIME_WINDOW]
    if len(recent_attempts) >= THRESHOLD:
        logging.warning(f"Brute-force attack detected from IP: {recent_attempts[0]['ip']}")
    else:
        logging.info("No brute-force attack detected.")

detect_brute_force(login_attempts)

# Case Study 2: Geo Anomalies
# Scenario: Detecting impossible travel based on login locations.
import geopy.distance

# Simulated login locations
logins = [
    {"user": "jdoe", "location": (37.7749, -122.4194), "timestamp": datetime.now() - timedelta(hours=1)},  # San Francisco
    {"user": "jdoe", "location": (40.7128, -74.0060), "timestamp": datetime.now()},  # New York
]

# Function to detect impossible travel
def detect_impossible_travel(logins):
    if len(logins) < 2:
        return

    for i in range(1, len(logins)):
        loc1 = logins[i - 1]['location']
        loc2 = logins[i]['location']
        time_diff = (logins[i]['timestamp'] - logins[i - 1]['timestamp']).total_seconds() / 3600  # in hours
        distance = geopy.distance.distance(loc1, loc2).km
        speed = distance / time_diff if time_diff > 0 else float('inf')

        if speed > 900:  # Assume impossible speed > 900 km/h
            logging.warning(f"Impossible travel detected for user {logins[i]['user']} between {loc1} and {loc2}.")
        else:
            logging.info("No impossible travel detected.")

detect_impossible_travel(logins)

# Case Study 3: Privilege Usage
# Scenario: Detecting unusual privilege escalation.
privilege_events = [
    {"user": "jdoe", "action": "read", "resource": "file1.txt", "timestamp": datetime.now() - timedelta(minutes=30)},
    {"user": "jdoe", "action": "write", "resource": "file1.txt", "timestamp": datetime.now() - timedelta(minutes=20)},
    {"user": "jdoe", "action": "admin", "resource": "server1", "timestamp": datetime.now() - timedelta(minutes=10)},
]

def detect_privilege_escalation(events):
    for event in events:
        if event['action'] == 'admin':
            logging.warning(f"Privilege escalation detected for user {event['user']} on resource {event['resource']}.")

detect_privilege_escalation(privilege_events)

# Case Study 4: Access Frequency
# Scenario: Detecting unusual access frequency to a resource.
access_logs = [
    {"user": "jdoe", "resource": "database", "timestamp": datetime.now() - timedelta(minutes=i)} for i in range(60)
]

ACCESS_THRESHOLD = 50

def detect_unusual_access_frequency(logs):
    recent_access = [log for log in logs if log['timestamp'] > datetime.now() - timedelta(hours=1)]
    if len(recent_access) > ACCESS_THRESHOLD:
        logging.warning(f"Unusual access frequency detected for resource {recent_access[0]['resource']}.")
    else:
        logging.info("No unusual access frequency detected.")

detect_unusual_access_frequency(access_logs)