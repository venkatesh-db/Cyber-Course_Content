# Placeholder for bot detection logic

def detect_bot_activity(log_entry):
    """
    Detect bot activity based on predefined patterns.

    Args:
        log_entry (dict): A single log entry.

    Returns:
        dict: The log entry with bot detection results.
    """
    bot_detected = False
    bot_reason = ""

    # Rule 1: High API request rate
    if log_entry.get("api_request_rate", 0) > 100:
        bot_detected = True
        bot_reason = "High API request rate"

    # Rule 2: Known bot user-agent
    if log_entry.get("user_agent", "").lower() in ["bot", "crawler", "spider"]:
        bot_detected = True
        bot_reason = "Known bot user-agent"

    log_entry["bot_detected"] = bot_detected
    log_entry["bot_reason"] = bot_reason
    return log_entry

if __name__ == "__main__":
    # Example usage
    sample_logs = [
        {"api_request_rate": 150, "user_agent": "Mozilla/5.0"},
        {"api_request_rate": 50, "user_agent": "bot"},
        {"api_request_rate": 10, "user_agent": "crawler"}
    ]
    for log in sample_logs:
        result = detect_bot_activity(log)
        print(result)