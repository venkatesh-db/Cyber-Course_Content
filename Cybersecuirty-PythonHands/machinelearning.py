
# every file type have different data structures 
# Python - Tuple , list , dict 

smile= 5 # 4 bytes of memory
import sys
print("size of 5",sys.getsizeof(smile)) # print the size of the variable in bytes

# pandas - dataframe - New data structure 
# numpy - array - New data structure

import numpy as np 

X=np.array([1,2,3,4,5]) # create array from list 
print(X) # print the array
print(X[0])
print(type(X)) # print the type of the array

print("size of numpy array element",sys.getsizeof(X[1]))


# Linear search Algorithm - O(n) time complexity
# binary search Algorithm - O(log n) time complexity

nums=[11,2,3,41,5] # list of numbers
nums.sort()
print(nums)

nums.sort(reverse=True) # sort in descending order
print(nums)

sorted_nums=sorted(nums) # sorted function returns a new sorted list
print(sorted_nums)



# np array 

X= np.array([[1],[2],[3]] )
print("ml array1",X)

Y= np.array( [2,3,4])
print("ml array2",Y)


# Machine learning algorithms - LinearRegression  
# LinearRegression -> take input of nparray 
from sklearn.linear_model import LinearRegression

model= LinearRegression() # create an instance of the model
model.fit(X,Y) # fit the model to the data

print("ml prediction:", model.predict([[5]])) # predict the output for the input data
print("ml prediction:", model.predict([[1]]))