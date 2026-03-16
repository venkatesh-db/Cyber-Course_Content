

import json 

def load_logs():
    print("Loading logs...")
    with open("logs/auth_logs.json") as file:
        logs = json.load(file)
    return logs