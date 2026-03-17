from datetime import datetime

def normalize_log(log_entry):
    """
    Normalize a log entry into a common schema.

    Args:
        log_entry (dict): The log entry to normalize.

    Returns:
        dict: The normalized log entry.
    """
    normalized_log = {
        "event_id": log_entry.get("transaction_id", "N/A"),
        "timestamp": log_entry.get("timestamp", datetime.utcnow().isoformat()),
        "source_system": log_entry.get("source_system", "unknown"),
        "user_id": log_entry.get("customer_id", "N/A"),
        "device_id": log_entry.get("device_id", "N/A"),
        "ip_address": log_entry.get("ip_address", "N/A"),
        "event_type": log_entry.get("event_type", "N/A"),
        "transaction_amount": log_entry.get("amount", 0.0),
        "geo_location": log_entry.get("geo_location", "N/A"),
        "api_endpoint": log_entry.get("api_endpoint", "N/A"),
        "status": log_entry.get("status", "N/A")
    }
    return normalized_log

if __name__ == "__main__":
    # Example usage
    sample_log = {
        "transaction_id": "12345",
        "customer_id": "67890",
        "amount": 100.0,
        "ip_address": "192.168.1.1",
        "event_type": "payment"
    }
    normalized_log = normalize_log(sample_log)
    print(f"Normalized log: {normalized_log}")