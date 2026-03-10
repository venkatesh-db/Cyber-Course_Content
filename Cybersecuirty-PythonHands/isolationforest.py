
# Isolation forest - cybersecurity anomaly detection
# susipicious login attempts
# abnormal network traffic
# fraud detection in financial transactions

# dataset - 10,12,11,13,12,100 
# very different from rest of the data points
# isolation forest can identify this as an anomaly

# ouput 1 - normal
# output -1 - anomaly


import numpy as np
from sklearn.ensemble import IsolationForest


data =[ [10],[12],[11],[13],[12],[100]]

model= IsolationForest()  # assuming 20% of the data is anomalous
model.fit(data)

prediction=model.predict(data)
print("anomaly",prediction)  # Output: [ 1  1  1  1  1 -1]