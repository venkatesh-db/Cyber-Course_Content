import json

def validate_log_schema(log_entry, required_fields):
    """
    Validate the schema of a log entry.

    Args:
        log_entry (dict): The log entry to validate.
        required_fields (list): List of required fields in the log schema.

    Returns:
        bool: True if the log entry is valid, False otherwise.
    """
    for field in required_fields:
        if field not in log_entry:
            return False
    return True

def parse_logs(logs, required_fields):
    """
    Parse and validate a list of logs.

    Args:
        logs (list): List of log entries.
        required_fields (list): List of required fields in the log schema.

    Returns:
        list: A list of valid log entries.
    """
    valid_logs = []
    for log in logs:
        if validate_log_schema(log, required_fields):
            valid_logs.append(log)
        else:
            print(f"Invalid log entry: {log}")
    return valid_logs

if __name__ == "__main__":
    # Example usage
    sample_logs = [
        {"transaction_id": "12345", "customer_id": "67890", "amount": 100.0},
        {"transaction_id": "54321", "amount": 50.0}  # Missing customer_id
    ]
    required_fields = ["transaction_id", "customer_id", "amount"]
    valid_logs = parse_logs(sample_logs, required_fields)
    print(f"Valid logs: {valid_logs}")