# Context information
context = {
    "userrole": "admin",
    "accesstime": "10:00am",
    "location": "office network",
    "log": "user accessed admin panel"
}

# Function to determine if the activity is suspicious
def is_suspicious(context):
    # Define suspicious conditions
    suspicious_conditions = [
        context["userrole"] != "admin",  # Non-admin trying to access admin panel
        context["location"].lower() != "office network",  # Access from outside the office network
        "accessed admin panel" not in context["log"].lower()  # Log does not match expected activity
    ]

    # Check if any condition is met
    return any(suspicious_conditions)

# Check if the activity is suspicious
if is_suspicious(context):
    print("Suspicious activity detected!")
else:
    print("Activity is normal.")