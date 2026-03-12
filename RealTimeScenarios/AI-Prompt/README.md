# Python SOC Automation Simulation Project

## Project Overview
This project simulates a Security Operations Center (SOC) automation workflow using Python. It processes large log files (~8GB) and implements detection rules for various cybersecurity scenarios. The pipeline mimics a SOC workflow, including log parsing, alert generation, SIEM-like filtering, and automated incident response.

## Features
1. **Log Processing**:
   - Windows Firewall logs
   - Linux system logs
   - Email logs
   - Malware process activity logs

2. **Cybersecurity Scenarios**:
   - **Scenario 1**: Windows firewall port scanning attack
   - **Scenario 2**: Linux SSH brute force attack
   - **Scenario 3**: Malware process creating shared memory and communicating with hidden processes
   - **Scenario 4**: Data exfiltration via suspicious outbound traffic

3. **SOC Workflow Simulation**:
   - Server logs arrive
   - Python script parses logs
   - Logs converted to pandas DataFrame
   - Detection rules applied
   - Suspicious alerts generated
   - Alerts reduced using SIEM-like filtering
   - Alerts sent to a GenAI module for explanation
   - SOC analyst decision
   - Incident ticket creation
   - Automated response triggered

4. **Detection Rules**:
   - Custom rules for each scenario.

5. **Output**:
   - Alert description
   - Severity level
   - Recommended action

6. **Incident Automation**:
   - Create incident ticket
   - Block IP
   - Isolate server

## Project Structure
```
AI-prompt/
├── logs/                # Sample log files
├── scripts/             # Python scripts for log processing and detection
├── outputs/             # Generated alerts and incident tickets
├── README.md            # Project documentation
```

## Requirements
- Python 3.8+
- pandas
- smtplib (for email notifications)
- subprocess (for automated responses)

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install pandas`.
3. Run the main script: `python scripts/main.py`.

## Future Enhancements
- Integration with real SIEM tools.
- Advanced GenAI module for alert explanation.
- Support for additional log formats.