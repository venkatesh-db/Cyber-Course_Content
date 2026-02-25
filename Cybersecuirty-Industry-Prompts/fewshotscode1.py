# List of email subjects
email_subjects = [
    "reset your password",
    "team lunch tomorrow",
    "verify your bank account now"
]

# Keywords commonly found in phishing or suspicious emails
suspicious_keywords = [
    "reset", "password", "verify", "bank", "account", "now", "urgent", "immediate", "action"
]

# Function to identify threats in email subjects
def identify_threats(subjects, keywords):
    threats = []
    for subject in subjects:
        if any(keyword in subject.lower() for keyword in keywords):
            threats.append(subject)
    return threats

# Identify threats
threatening_subjects = identify_threats(email_subjects, suspicious_keywords)

# Display results
if threatening_subjects:
    print("Potential threats detected in the following email subjects:")
    for subject in threatening_subjects:
        print(f"- {subject}")
else:
    print("No threats detected in the email subjects.")