
#variable describe security behaviour 

'''

failedlogins       loginfailures 
acessfrequency      ofen user acess system 
geoamomaly.         Login from unusual location
priveligeusage      admin command execution 

'''

'''

Log to features 

2026-03-10 10:02:01 user=raj ip=192.168.1.2 action=login  status=failed

user=raj
failedlogins=1
ip=192.168.1.2
action=login

'''

from collections import defaultdict
data =["login","login","logout","login"]

# inbuilt data structures 
count=defaultdict(int)

for i in data:
    count[i]+=1 
    
print(count)

logs=[
    "user=raj status=failed",
    "user=raj status=failed",
    "user=venkat status=failed",
    "user=admin status=sucess",
]

failed=defaultdict(int)

for log in logs:
    parts= log.split()
    print("dafult venkat",parts)
    
    user= parts[0].split("=")[1]
    status=parts[1].split("=")[1]
    
    if status=="failed":
        failed[user]+=1
        
print(failed)
    
    
    
    
