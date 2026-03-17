def block_ip(ip_address):
    """
    Block a malicious IP address.

    Args:
        ip_address (str): The IP address to block.

    Returns:
        dict: Action result.
    """
    # Simulate blocking the IP address
    action_result = {
        "action": "block_ip",
        "ip_address": ip_address,
        "status": "success",
        "message": f"IP address {ip_address} has been blocked."
    }
    print(action_result["message"])
    return action_result

if __name__ == "__main__":
    # Example usage
    sample_ip = "192.168.1.1"
    result = block_ip(sample_ip)
    print("Action Result:", result)