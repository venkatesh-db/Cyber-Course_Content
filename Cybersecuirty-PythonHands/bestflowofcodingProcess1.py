

# step1- Load packages
# step2 - file types 
# focus3  -> excution of code with files type 
# focus 4  --> work on with diffreent data structures & algotthims 

import  logging 
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from datetime import datetime,timedelta


def isolation_forest_analysis(transactions):

  data= np.array( [[ t["id"],t["amount"]] for t in transactions ])

  # data tranformation list of dict in to numpy array
  # normal data - 80%
  #anamolies - 20%
  
  model=IsolationForest(contamination=0.2,random_state=42)
  model.fit(data)
  
  #predict anomalies 
  
  pred = model.predict(data)
  for i , prediction in enumerate(pred):
      if prediction == -1:
          print(f"Transaction {transactions[i]['id']} is an anomaly with amount {transactions[i]['amount']}")
      else :
            print(f"Transaction {transactions[i]['id']} is normal with amount {transactions[i]['amount']}")
  

def explain_model(clf,transactions):

   scores = clf.decision_function(np.array([[t["id"],t["amount"]] for t in transactions]))
   
   for i, score in enumerate(scores):
         print(f"Transaction {transactions[i]['id']} has anomaly score: {score}")
        
 
def fiserv_use_cases():
     
     trancations=[
         {"id":1,"amount":1000,"timestamp":"2023-01-01 10:00:00"},
         {"id":2,"amount":5000,"timestamp":"2023-01-01 11:00:00"},
         {"id":3,"amount":200,"timestamp":"2023-01-01 12:00:00"},
         {"id":4,"amount":7000,"timestamp":"2023-01-01 13:00:00"},
         {"id":5,"amount":300,"timestamp":"2023-01-01 14:00:00"},
     ]
     
     isolation_forest_analysis(trancations)
     
     clf=IsolationForest(contamination=0.2,random_state=42)
     clf.fit(np.array([[t["id"],t["amount"]] for t in trancations]))
     explain_model( clf,trancations)


fiserv_use_cases()