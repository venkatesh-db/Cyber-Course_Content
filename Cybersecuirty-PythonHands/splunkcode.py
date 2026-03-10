

import splunklib.client as client
import splunklib.results as results

# connect to splunk server
# pcap file analysis with scapy
# darktrace - machine learning anomoly detection

'''

logs 
 |
 python processing 
 |
 machine learning 
  |
  alert system 
  |
  dashboard grafana 
 '''


service=client.connect(
    host="localhost",
    port=8089,
    username="admin",
    password="changeme"
)

from scapy.all import sniff 

def packet_analyser(packet):
    
    



