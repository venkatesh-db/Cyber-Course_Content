from ip_reputation import check_ip_reputation
from bot_detection import detect_bot_activity

def test_threat_intelligence():
    # Test IP Reputation
    print("Testing IP Reputation...")
    sample_ips = ["192.168.1.1", "10.0.0.1", "8.8.8.8"]
    for ip in sample_ips:
        result = check_ip_reputation(ip)
        print(result)

    # Test Bot Detection
    print("\nTesting Bot Detection...")
    sample_logs = [
        {"api_request_rate": 150, "user_agent": "Mozilla/5.0"},
        {"api_request_rate": 50, "user_agent": "bot"},
        {"api_request_rate": 10, "user_agent": "crawler"}
    ]
    for log in sample_logs:
        result = detect_bot_activity(log)
        print(result)

if __name__ == "__main__":
    test_threat_intelligence()