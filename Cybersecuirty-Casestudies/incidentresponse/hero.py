

import requests

def call_mallware_api():
    
    url="http://localhost:8001/detect"
    response=requests.get(url)
    data = response.json()
    print("alerts from api",data)
    
if __name__ == "__main__":
    call_mallware_api()
    
    