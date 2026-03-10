
def  Smile()->str:
    print("Smile") # execute 1 line 
    return "Bug"   # execute 2nd line and return the value to the caller
    
ret=Smile() # call the function to execute 1 line it 
# ret will hold the value returned by the function which is "Bug"
print(ret) # print the value stored in ret which is "Bug"


fd=open("file.txt","w") # execute 1 line to open the file in write mode
fd.writelines("Hello World") # execute 1 line to write "Hello World" to the file
fd.close() # execute 1 line to close the file


class Incident:
    
    def resolvingteam(self)->str:
        print("Resolving Team") # execute 1 line 
        return "Team" # execute 2nd line and return the value to the caller
    def production(self)->Incident:
        return Incident() # execute 1 line to return the object of the class Incident to the caller


chandan= Incident()
ret=chandan.resolvingteam()     
# call the method to execute 1 line it
print(ret) # print the value stored in ret which is "Team"
       

objects=chandan.production()
print(objects) # print the object of the class Incident which is returned by the method production()

 
beautifulsmiles="smiles"
# internally beautifulsmiles =str("smiles")  

x=10
# internally x=int(10)

IamHero="pythonvanhaseulem superman batman"
Herotwo=IamHero

# how many objects are created in the above code?

import sys
print( sys.getrefcount(IamHero)) # to check the reference count of the object "python" which is created in the memory

del IamHero # delete the reference variable IamHero
print( sys.getrefcount(Herotwo)) # to check the reference count of the
