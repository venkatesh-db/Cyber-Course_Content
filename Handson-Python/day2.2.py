import pandas 

data = {
          "tciketid": [ "sms12344" ,"sms124555"],
          "serverity": [ "high" , "low"],
          "description":["server is trggieed with logins", "windows or cloud server" ]
}

# objecr creation pandas 

newdatassturcture=pandas.DataFrame(data)  # dict is tranformed in to new data frame's
print(newdatassturcture)

# methods 

print( newdatassturcture.columns) # keys are named as columns 
print(newdatassturcture["tciketid"] )


text="My number is 9900367097"
pattern=r"\d{10}"

import re 

match=re.search(pattern, text)
if match:
    print("match found",match.group())


text="Dates: 12-05-2025 , 01-01-2025"
dates=re.findall(r"\b\d{2}-\d{2}-\d{4}\b",text)

# b - start of word boundary , end of word boundary 
# r - raw string 
#d - digit 0-9 
#b - match starts end 

print("final smiles ", dates)

