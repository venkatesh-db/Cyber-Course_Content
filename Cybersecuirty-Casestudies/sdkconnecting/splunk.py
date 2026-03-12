

# pip install splunk-sdk


import splunklib.client as client
import splunklib.results as results


service =client.connect(
    host="localhost",
    port=8089,
    username="admin",
    password="changeme",
    scheme="https"
)

print("Connected to Splunk")
