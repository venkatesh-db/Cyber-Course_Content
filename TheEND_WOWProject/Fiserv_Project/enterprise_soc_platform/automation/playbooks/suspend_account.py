# Placeholder for playbook to suspend account

def suspend_account(account_id):
    """
    Suspend a suspicious account.

    Args:
        account_id (str): The account ID to suspend.

    Returns:
        dict: Action result.
    """
    # Simulate suspending the account
    action_result = {
        "action": "suspend_account",
        "account_id": account_id,
        "status": "success",
        "message": f"Account {account_id} has been suspended."
    }
    print(action_result["message"])
    return action_result

if __name__ == "__main__":
    # Example usage
    sample_account = "user123"
    result = suspend_account(sample_account)
    print("Action Result:", result)