# Placeholder for IP reputation logic

def check_ip_reputation(ip_address):
    """
    Check the reputation of an IP address.

    Args:
        ip_address (str): The IP address to check.

    Returns:
        dict: Reputation details of the IP address.
    """
    # Example reputation database
    reputation_db = {
        "192.168.1.1": {"reputation": "malicious", "reason": "Known botnet IP"},
        "10.0.0.1": {"reputation": "suspicious", "reason": "High traffic from this IP"}
    }

    if ip_address in reputation_db:
        return {
            "ip_address": ip_address,
            "reputation": reputation_db[ip_address]["reputation"],
            "reason": reputation_db[ip_address]["reason"]
        }
    else:
        return {
            "ip_address": ip_address,
            "reputation": "unknown",
            "reason": "No data available"
        }

if __name__ == "__main__":
    # Example usage
    sample_ips = ["192.168.1.1", "10.0.0.1", "8.8.8.8"]
    for ip in sample_ips:
        result = check_ip_reputation(ip)
        print(result)