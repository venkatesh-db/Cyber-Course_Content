

# question    answer   data where store in Brain 
howareyou   =  "good"
# variable     data          coder data  in RAM              


Trainername= "venkatesh"      # Data  separted in memory 
exp       =  16               # data  separted in memory 
Location  =  "bangalore"      # Data  separted in memory 
number    =  8                # 8- data 


#  data toegthere in memory - array list dict class object
#  venkatesh 16 bangalore 
#  human data vs Python Data --> Syntax 

# Syntax --> symbol or keywords 

#Data --> only symbols 

smiles=5

'''

""  -- string 
9 3.14 - .
( )  - tuple 
[ ]  - List
{ }  - dict 

'''


# keyword many symbols --> terminiologies of python 

'''

function 
class
methods 
objects 


'''



'''
Goal - > 5 lines of code 

'''

Trainer_name= "venkatesh"      # Data  separted in memory 
exp       =  16               # data  separted in memory 
Location  =  "bangalore"      # Data  separted in memory 
number    =  8                # 8- data 
enjoying  =  True



'''

Goal - > 10 lines of code 


'''

def  Trainer_Profile():  # define a function 

    # what is identation
    # below complete code belong to block - Trainer_Profile

    Trainer_name= "venkatesh"      # Data  separted in memory 
    exp       =  16               # data  separted in memory 
    Location  =  "bangalore"      # Data  separted in memory 
    number    =  8                # 8- data 
    enjoying  =  True
    trainerworking= "NPCI"                     # Data  separted in memory 
    trainingdeliveerd    =  118               # data  separted in memory 
    cities =    [ "bangalore" , "hyderbad" ]    # Data  separted in memory 
    totaldays    =  10                # 8- data 
    timing =  "2-6 pm"
    print("nodia boys")  # inside the block


print("finserv smiles")  # outside of the block 


# python smiles.py --->  77 line of code 
# Line 66 - 77  only defined functioon 

#Trainer_Profile() # funcytion call  inside block code executes 

 # Data  separted in memory 

cocnut =1
flowers="rose"
malla = "chanmthi mala"

print(malla) # acessing variables

 # Data  Together in continous memory - Fixed 

offering = ( "1 cocunyt","roses","1 chaanmathi mala" ) # tuple 
print(offering[2]) #acessing index 

 # Data  Together in continous memory - Infinite 

balaofferings= [  "1 cocunyt","roses","1 chaanmathi mala" ] # list 
otherdevotess="lotusflower"
balaofferings.append("lotusflowrs")       # offering indiviudally 
balaofferings.append(["tulsi","1 gheee"])  # offering toether 
balaofferings.append("500 rs")             # offering indiviudally
print(balaofferings[3]) # acessing index
print(balaofferings)


# 3 login failed 

Logs= [
        "login fail ip=162.168.1.10",
        "login fail ip=192.168.1.10",
        "login sucess ip =163,18.19.10"
]

# terminology - Loops 
count =0

for i in Logs : # one ip address 

    # i -at a time  it holds one index value only   logs - continous index 0,1,2 
    # i will iterate 3 index's

    # conditions 
    if  "login fail" in i :  # search for  "login fail" in   "login fail ip=162.168.1.10" if present it executes 2 lines 
        print("failed ")
        count=count+1
    print(i)
 
print("fail logs",count)

machine = ("webserver-1","10.0.0.5","ubtnuituy","prduction","nignix")
print(machine[1])


# Infinite data each data has unique key
Owncar = {"driverseat":"venkatesh" ,"frontseat":"brother","backsidemiddle":"mother","backleft":"spouse","backright":"father" }

# we are acessing with key not index 

print(Owncar["frontseat"])
swapseat=Owncar["backsidemiddle"]  # variable hold mother 
Owncar["backsidemiddle"] = Owncar["frontseat"]
Owncar["frontseat"] = swapseat
print(Owncar)


venkatesh_gold= {"ring":["balaji","king","ring2"] , "neck": ("cut chain","small chain"), "brcelet":"jjaguar braclelet"}

for key,value in venkatesh_gold.items():
    # key value -> hold only one key and one value at atime ->   # 3 keys , 3 values 
    print( key,value)

# real production

failed_attempts ={
    "192.168.1.10":2,
    "10.0.0.5":1
}

incidents ={
    "ip":"192.68.1.0",
    "severity":"high",
    "type":"brute force",
    "status":"open",
    "threat":"sql injection"
}

for i in incidents.keys():
    # i -> one key --> 5 key's 
    print(i)


# Incident1 -> logs 
# analyse the log  --> Efforts : 40 min , 4-5 hours 


# what all we check in logs 
# 1.source 2. dest 3. payload 4. entitye 5. file path 6. url 


# File data  -->  JSON  --> Which Data structures --> Dict  
# File data   --> log  --> Which Data structures --> List ,Dict 
# File data   --> syslog -->Which Data structures --> 


#  Logs data  -->  Harddisk 
#                 tools Splunk
# 
#  Local storage ||  network storage || cloud storage 
#         Handson 
# 
#      

logentry="2026-02-23 alert supscious login from 192.168.1.10\n"   # ram 

# copy the log fromm ram to harddisk s

file=open("soc_logs.txt","a")  # mandatory w -write r-read  a -WRITE APPEND 
file.write(logentry)          # what lines --> string -> ram --> data copied in to harddisks
file.close()                  # close the resource haddisk other can open file 


file1=open("soc_logs.txt","r")
ot=file1.readlines()  #  read from harddisk and copy in to ram variable ot


'''
2026-02-23 alert supscious login from 192.168.1.10
2026-02-23 alert supscious login from 192.168.1.10
2026-02-23 alert supscious login from 192.168.1.10
2026-02-23 alert supscious login from 192.168.1.10
2026-02-23 alert supscious login from 192.168.1.10
2026-02-23 alert supscious login from 192.168.1.10

'''

print(ot)
file1.close()

'''
FileNotFoundError: [Errno 2] No such file or directory: 'soc_logs1.txt'
'''


'''
advanced logs 

user behaviour 
network flows 
api calls 
threat intyteggience matches 


'''

logs= [
    
    "Process=powershell.exe command=powershell -enc aw52b2tl",
    "Process=chrome.exe command=normal browsing ",
    ]

for log in logs :
    if "powershell.exe" in log  and "-enc" in log :
        print("supicious alert")

# log sources

endpointlogs=[
     { "source":"endpoint","event":"loginfail","ip":"192.168,1.10" },
     { "source":"endpoint","event":"powershell","ip":"191.168,1.10" }
    ]

networklogs=[
     { "source":"newtwork","event":"port","ip":"192.168,1.10"},
    ]
    
cloud_logs=[
    {"source":"cloud","event":"unauthorized_apicall","ip":"52.12.13"},
    ]

# log collector 

def colect_logs():
    collected =endpointlogs+networklogs+cloud_logs
    # scope is with limited to function return to acess outside 
    return collected

def normalise_logs(logs):
     normalises=[]

     for log in logs:
        normalises.append( {
            "source": log["source"],
            "event": log["event"],
            "ip":log["ip"],
            "severity":"low"
             })
     return normalises

def detect_threats():
    pass

def repsondincidents():
    pass


logs=colect_logs()
print("logs",logs)
newvalue=normalise_logs(logs)
print("newvalues:",newvalue)

