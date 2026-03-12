import xmltodict
import json
import pandas as pd
import yara
import requests
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Parse Windows Event Logs
def parse_event_log(event_xml):
    """Parse XML event log into a dictionary."""
    event_dict = xmltodict.parse(event_xml)
    print("Parsed Event Dictionary:", event_dict)
    return event_dict

# Step 2: Convert to JSON
def convert_to_json(event_dict):
    """Convert dictionary to JSON."""
    print("Event Dictionary before JSON conversion:", event_dict)
    return json.dumps(event_dict, indent=4)

# Step 3: Data Analysis
def analyze_data(event_dict):
    """Analyze event data using pandas."""
    df = pd.DataFrame([event_dict])
    print("DataFrame:", df)
    return df

# Step 4: Detection Engine
def yara_detection(event_data, rule_path):
    """Apply YARA rules to detect threats."""
    absolute_rule_path = os.path.join(os.path.dirname(__file__), rule_path)
    rules = yara.compile(filepath=absolute_rule_path)
    matches = rules.match(data=event_data)
    return matches

# Step 5: Threat Intelligence
def query_virustotal(file_hash):
    """Query VirusTotal for threat intelligence."""
    api_key = "<YOUR_API_KEY>"
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

# Step 6: Feature Extraction
def extract_features(event_dict):
    """Convert event dictionary into numerical features."""
    features = []
    
    # Example feature extraction: Count the number of keys in the event data
    features.append(len(event_dict.get('EventData', {}).keys()))

    # Example: Check if specific fields exist
    features.append(1 if 'ProcessId' in event_dict.get('EventData', {}) else 0)
    features.append(1 if 'CommandLine' in event_dict.get('EventData', {}) else 0)

    # Example: Length of the CommandLine field
    command_line = event_dict.get('EventData', {}).get('CommandLine', '')
    features.append(len(command_line))

    return features

# Step 7: Machine Learning Detection (Updated with Training)
def ml_detection(features):
    """Train and apply ML model for detection."""
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    # Example dataset for training
    X = [[0, 0, 0, 0], [1, 1, 1, 10], [0, 1, 0, 5], [1, 0, 1, 15]]  # Features
    y = [0, 1, 1, 0]  # Labels

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))

    # Predict on the provided features
    return model.predict([features])

# Step 8: Kafka Streaming
def stream_to_kafka(topic, data):
    """Stream data to Kafka."""
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send(topic, value=data.encode('utf-8'))
    producer.close()

# Step 9: SIEM Integration
def send_to_siem(data):
    """Send data to Elastic or Splunk."""
    print("Sending data to SIEM:", data)

# Example Usage
if __name__ == "__main__":
    event_xml = r"""
<Event>
  <System>
    <Provider Name="Sysmon" />
    <EventID>1</EventID>
    <Computer>WIN-SERVER01</Computer>
  </System>
  <EventData>
    <Data Name="UtcTime">2026-03-11 10:15:22.120</Data>
    <Data Name="ProcessGuid">{A1B2C3D4-E5F6-7890-1122-334455667788}</Data>
    <Data Name="ProcessId">4280</Data>
    <Data Name="Image">C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe</Data>
    <Data Name="User">WIN-SERVER01\\jaymin.m</Data>
    <Data Name="CommandLine">powershell.exe Get-Process -Name svchost</Data>
  </EventData>
</Event>
"""

    # Parse and analyze
    event_dict = parse_event_log(event_xml)
    event_json = convert_to_json(event_dict)
    df = analyze_data(event_dict)

    # Detection
    yara_matches = yara_detection(event_json, "rules.yar")
    print("YARA Matches:", yara_matches)

    # Threat Intelligence
    vt_result = query_virustotal("sample_file_hash")
    print("VirusTotal Result:", vt_result)

    # Machine Learning
    features = extract_features(event_dict)
    ml_result = ml_detection(features)
    print("ML Detection Result:", ml_result)

    # Streaming and SIEM
    #stream_to_kafka("sysmon_events", event_json)
   #send_to_siem(event_json)