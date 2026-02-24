


import json 
print(json)

#C:\Program Files\Python313\Lib\json


from json import decoder  # importing code design
print(decoder)

# code execution here

chandan=decoder.JSONDecoder() # object creation
print(chandan)
json_str = '{"name": "Alice", "age": 30, "city": "Wonderland"}'  # string 
ret=chandan.decode(json_str) # string which has dict
print(ret)         # output comes in dict 
print( type(ret))  # type of the objects


greatcompany= " fiserv is world best Fintech Company "
print( greatcompany.capitalize() )
print( greatcompany.lower() )

print(greatcompany.find("best"))
print(greatcompany.index("best"))

print(greatcompany.lstrip())
print(greatcompany.rstrip())
print(greatcompany.strip())

new_text=greatcompany.replace("best","great")
print(new_text)

data="ravi,anil,sunil"
newstexts=data.split(",")
print(newstexts)

comp= "fiserv is world best Fintech Company"
newstexts=comp.split(" ")
print(newstexts)

joined="-".join(newstexts)
print(joined)

url="https://example.com"

print( url.startswith("https"))
print(url.endswith(".com"))

log = " ERROR: Failed login from 192.168.1.1  "

cleanlog=log.strip().replace("ERROR:","ALERT:")
print(cleanlog)

