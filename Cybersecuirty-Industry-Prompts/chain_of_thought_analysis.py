def analyze_login_suspicion(user_details):
    """
    Analyze login details step-by-step to determine if the login is suspicious based on security rules.

    Args:
        user_details (dict): A dictionary containing user details such as role, login time, location, and failed attempts.

    Returns:
        dict: A dictionary containing the analysis for each rule and the final decision.
    """
    analysis = {}

    # Rule 1: Evaluate login time
    login_time = user_details.get("login_time")
    if login_time:
        hour = int(login_time.split(":")[0])
        if hour < 6 or hour > 22:
            analysis["login_time"] = "Suspicious: Login time is outside the allowed range (6 AM - 10 PM)."
        else:
            analysis["login_time"] = "Normal: Login time is within the allowed range."
    else:
        analysis["login_time"] = "Unknown: Login time not provided."

    # Rule 2: Evaluate location
    location = user_details.get("location")
    role = user_details.get("role")
    if location == "foreign ip" and role != "admin":
        analysis["location"] = "Suspicious: Foreign IP access for non-admin user."
    else:
        analysis["location"] = "Normal: Location access is acceptable."

    # Rule 3: Evaluate failed attempts
    failed_attempts = user_details.get("failed_attempts", 0)
    if failed_attempts > 5:
        analysis["failed_attempts"] = "Suspicious: More than 5 failed login attempts indicate a potential brute-force attack."
    else:
        analysis["failed_attempts"] = "Normal: Failed attempts are within the acceptable range."

    # Rule 4: Evaluate user role
    if role == "employee" and location == "foreign ip":
        analysis["user_role"] = "Suspicious: Employees should not access remotely from foreign IPs."
    elif role == "admin":
        analysis["user_role"] = "Normal: Admin users are allowed remote access."
    else:
        analysis["user_role"] = "Normal: User role and access are acceptable."

    # Final decision
    suspicious_flags = [value for value in analysis.values() if "Suspicious" in value]
    if suspicious_flags:
        analysis["final_decision"] = "Suspicious login detected. Reasons: " + ", ".join(suspicious_flags)
    else:
        analysis["final_decision"] = "Login appears normal."

    return analysis

# Example usage
if __name__ == "__main__":
    user_details = {
        "role": "employee",
        "login_time": "2:00 am",
        "location": "foreign ip",
        "failed_attempts": 6
    }

    result = analyze_login_suspicion(user_details)
    for key, value in result.items():
        print(f"{key}: {value}")