# pip install splunk-sdk

import splunklib.client as client
import splunklib.results as results
import sys

'''

| Port     | Purpose          |
| -------- | ---------------- |
| **8000** | Splunk Web UI    | --soc analyst 

| **8089** | Splunk REST API  | 

| **9997** | Forwarder data   |- receive logs from forwarders (universal or heavy)


system logs 
security logs
application logs


endpoint logs 
|
universal forwader
|
splunk receiuver 
|
port 9997


| **514**  | Syslog ingestion |

network device 
||
syslog message
||
port 514
||
splunk server 



tranport protocol send system message to log collector 

firwall logs 
router logs 
linux servers


'''


try:
    service = client.connect(
        host="localhost",
        port=8089,
        username="coder",
        password="GlobalStar7",
        scheme="https"
    )
    print("Connected to Splunk")
except Exception as e:
    print("Failed to connect to Splunk:", e)
    sys.exit(1)


# 1. automotion of secuirty operations 

''' 
run log search
detect malware patteerns

python sdk 
|
splunk sdk
|
search logs 
|
alert soc team

'''

# 2. real time threat detection

'''
brute force attacks malware downlaods
'''

#3. integration with other security tools

'''
cloud logs 
firwall logs
'''

#4. custom security applications 

'''
automate incident response
soc investigation tool
threat intelligence platform
'''

# devops +security

'''devsecops'''
