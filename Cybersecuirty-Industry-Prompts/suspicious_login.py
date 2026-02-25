# Context information
context = {
    "official_login_hours": "9 to 21",  # Official login hours (9 AM to 9 PM)
    "logintime": 23  # User login time in 24-hour format
}

# Function to determine if the login time is suspicious
def is_suspicious_login(context):
    # Parse official login hours
    start_hour, end_hour = map(int, context["official_login_hours"].split(" to "))
    logintime = context["logintime"]

    # Check if the login time is outside official hours
    if logintime < start_hour or logintime > end_hour:
        return True
    return False

# Check if the login is suspicious
if is_suspicious_login(context):
    print("Suspicious login detected!")
else:
    print("Login is within official hours.")