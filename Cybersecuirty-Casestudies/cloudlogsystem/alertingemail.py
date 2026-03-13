
subject ="soc alerting email"

body="""
alert type : unaunthorised deletion of bucket detected
user:unknownuser 
ip: 45.33.22.1
action:deletebucket

plesse investigate the alert and take necessary actions to prevent further unauthorized activities.
"""


import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart


sender_email="your_email@example.com"
receiver_email="soc_team@company.com"
password="your_email_password"


msg=MIMEMultipart()
msg["From"]=sender_email
msg["To"]=receiver_email
msg["Subject"]=subject
msg.attach(MIMEText(body,"plain"))

#outlook smtp server 

smtpserver="smtp.office365.com"
port=587

server= smtplib.SMTP(smtpserver, port)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, msg.as_string())
server.quit()
