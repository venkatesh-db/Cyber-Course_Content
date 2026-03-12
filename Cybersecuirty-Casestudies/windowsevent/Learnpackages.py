

import xmltodict
'xml convert into dict'

# log is in xml file 

event_xml = r"""
<Event>
  <System>
    <Provider Name="Sysmon" />
    <EventID>1</EventID>
    <Computer>WIN-SERVER01</Computer>
  </System>
  <EventData>
    <Data Name="UtcTime">2026-03-11 10:15:22.120</Data>
    <Data Name="ProcessGuid">{A1B2C3D4-E5F6-7890-1122-334455667788}</Data>
    <Data Name="ProcessId">4280</Data>
    <Data Name="Image">C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe</Data>
    <Data Name="User">WIN-SERVER01\\jaymin.m</Data>
    <Data Name="CommandLine">powershell.exe Get-Process -Name svchost</Data>
  </EventData>
</Event>
"""

xml_dict = xmltodict.parse(event_xml)
#print(xml_dict)

import json 

json_data = json.dumps(xml_dict, indent=4)
#print(json_data)

import pandas as pd

df=pd.DataFrame([xml_dict])
print(df)


# data residing in xml

# traformation1- xml to dict 
# traformation2- dict to JSon 
# traformation3- xml_dict to dataframe

 