import os
import json 

# Get the absolute path of the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the JSON file
json_file_path = os.path.join(script_dir, "cloud_logs.json")

with open(json_file_path) as file:
    logs = json.load(file)
    
# stage1- open file type data of json file is loaded propely 

print(logs)

# stage 2 - check for the presence of specific keys in the logs and print their values

# stage 3 

alerts=[] 

for log in logs:
    
    if log["eventName"] == "DeleteBucket" and log["user"] != "admin":

# stage 3 - if the event name is "DeleteBucket", print the bucket name and the user who performed the action
  
       alerts.append({
           "type":"Critical",
           "message":"unauthorized deletion of bucket detected",
           "user":log["user"],
           "ip":log["sourceIPAddress"]
       })
       
for alert in alerts:
    print(f"ALERT: {alert['type']} - {alert['message']} by user {alert['user']} from IP {alert['ip']}")
    
    