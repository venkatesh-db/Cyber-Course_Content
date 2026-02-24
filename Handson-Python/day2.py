

def teamouting():

    # varibale location is visible to teamouting 
    location= "leelaplace"
    print(location)

#print(location)

teamouting()   # variable inside block will get meoory

class  Appraisal:

    # indetenetation belongs to class 
    deafualtrating= 7
    hikepercentage=10.1

    # variable is visible to outside class class variables -Automatically get memory when decalared 

print(Appraisal.hikepercentage)



'''
            team  -->  incidentresposne      --> repseresented class 
            
           common actvity --> mointroing        --> methods 

           people emploeyee --> raj , ankit     --> objects 

           Method call      ---> working on activity --> method call with objects 

           self              --> points to objects 

'''


class incidentresposne:

    def mointoring(self,issue):   # method is called one actvity performing repedeately daily
        # self points to team people --> objects
        self.tickets=issue
        

# the below line a new member joining a team 
raj = incidentresposne()  # object crreation represenattion of people team member

# new team mmeber working on new issue
raj.mointoring("server down issues") # each person work on diffrent tickets each ticket has different probelm decsriptions

ankith=incidentresposne()
ankith.mointoring("crash in infra") 


class cyberoperation:

    def threats(self):   # method is called one actvity performing repedeately daily
       
        pass


# Inherietnce 
# team communication cyberoperation team information need to be communciatred to anotehr team -> incidentresposne


class Fiserv:

    # log sources - class vraibles

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

    def colect_logs(self):
     collected =Fiserv.endpointlogs+Fiserv.networklogs+Fiserv.cloud_logs
      # scope is with limited to function return to acess outside 
     return collected

    def normalise_logs(self,logs):
     # isntance variable or object variables
     self.normalises=[]

     for log in logs:
        self.normalises.append( {
            "source": log["source"],
            "event": log["event"],
            "ip":log["ip"],
            "severity":"low"
             })
     return self.normalises
    
# code execution 

chandan =Fiserv()
ret=chandan.colect_logs()
ret2=chandan.normalise_logs(ret)
print(ret2)