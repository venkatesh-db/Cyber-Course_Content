import time

import splunklib.client as client
import splunklib.results as results
import sys

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
    

query = 'search index=_audit | table _time user action'

i=0
while i<1:
    print("running soc")

    try:
        job = service.jobs.create(query)
    except Exception as e:
        print("Failed to create job:", e)
        sys.exit(1)

    while not job.is_done():
        pass

    try:
        for result in results.ResultsReader(job.results()):
            print(f"Time: {result['_time']}, User: {result['user']}, Action: {result['action']}")
    except Exception as e:
        print("Failed to read results:", e)
        sys.exit(1)

    i=i+1
    #time.sleep(60)  # wait for 1 minute before running the next search