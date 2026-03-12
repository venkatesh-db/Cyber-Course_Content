import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from malwareendpointinfection import casestudy

app = FastAPI()

# url - http://localhost:8001/detect --> Function

@app.get("/detect")
def detect():
    
    alerts= casestudy.detect_malware(casestudy.logs)

    for alert in alerts:
     print("venkatesh alewerts",alert)
     
    return {"alerts": alerts}


@app.get("/handsome")
def suspicious():
    
    alerts= casestudy.detect_malware(casestudy.logs)

    for alert in alerts:
     print("venkatesh alewerts",alert)
     
    return {"smiling stories": alerts}

# pip install fastapi uvicorn

# /usr/local/bin/python3 -m uvicorn secuirtysystems.api:app --reload --port 8001 # server run

#                                    foldername     filename app variable name 

# server running works --> http://localhost:8001/detect -> api hits the function and returns the alerts in json format.
