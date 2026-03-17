import re

def mask_sensitive_fields(log_entry, sensitive_fields):
    """
    Mask sensitive fields in a log entry.

    Args:
        log_entry (dict): The log entry to mask.
        sensitive_fields (list): List of fields to mask.

    Returns:
        dict: The log entry with masked sensitive fields.
    """
    masked_log = log_entry.copy()
    for field in sensitive_fields:
        if field in masked_log and isinstance(masked_log[field], str):
            if field == "PAN":  # Mask card numbers
                masked_log[field] = re.sub(r"(\d{4})\d{8,12}(\d{4})", r"\1********\2", masked_log[field])
            else:
                masked_log[field] = "***MASKED***"
    return masked_log

if __name__ == "__main__":
    # Example usage
    sample_log = {
        "transaction_id": "12345",
        "customer_id": "67890",
        "PAN": "4111111111111111",
        "email": "customer@example.com"
    }
    sensitive_fields = ["PAN", "email"]
    masked_log = mask_sensitive_fields(sample_log, sensitive_fields)
    print(f"Masked log: {masked_log}")