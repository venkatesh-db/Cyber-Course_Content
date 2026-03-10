

teamperformance = {

    "incident_response": [ {"name":"venkat","exp":16,"rating":7.5 } , 
                          {"name":"raj","exp":6,"rating":8.0 }
                          ]
}            # [ List of dicts ] in RAM 

'''. Excel - incident_response

      name.   exp   rating.   # columns 

      venkat  16     7.5.     # rows 
      raj     6      8.0.     # rows 

'''

import pandas as pd

df=pd.read_csv("incident_response.csv")
print(df)

