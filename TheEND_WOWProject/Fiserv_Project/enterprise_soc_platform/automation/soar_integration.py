from .playbooks.block_ip import block_ip
from .playbooks.suspend_account import suspend_account
from .playbooks.notify_fraud_team import notify_fraud_team

def execute_playbook(action, **kwargs):
    """
    Execute a specific playbook action.

    Args:
        action (str): The playbook action to execute (e.g., 'block_ip', 'suspend_account', 'notify_fraud_team').
        kwargs: Additional arguments for the playbook.

    Returns:
        dict: Action result.
    """
    if action == "block_ip":
        return block_ip(kwargs.get("ip_address"))
    elif action == "suspend_account":
        return suspend_account(kwargs.get("account_id"))
    elif action == "notify_fraud_team":
        return notify_fraud_team(kwargs.get("incident_id"), kwargs.get("details"))
    else:
        return {
            "action": action,
            "status": "failure",
            "message": "Unknown action."
        }

if __name__ == "__main__":
    # Example usage
    print("Executing SOAR Playbooks:")

    # Block IP example
    block_result = execute_playbook("block_ip", ip_address="192.168.1.1")
    print("Block IP Result:", block_result)

    # Suspend account example
    suspend_result = execute_playbook("suspend_account", account_id="user123")
    print("Suspend Account Result:", suspend_result)

    # Notify fraud team example
    notify_result = execute_playbook("notify_fraud_team", incident_id="INC12345", details="Suspicious login attempts detected.")
    print("Notify Fraud Team Result:", notify_result)