# suppose you have a database of users and you want to send them emails based on their interests



"""
Tasks to be done:
1. import the required classes 
    (MIME : Multipurpose Internet Mail Extensions)
    It is an Internet standard that extends the format of email to support: Text in character sets other than ASCII. Non-text attachments: audio, video, images, application programs etc. Message bodies with multiple parts.
    It is purely a format to define the emails and has nothing to do with python
2. make the required message
3. connect to a SMTP server to send emails
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text()) # to replace parameters in html dynamically
# template.substitute()()

message = MIMEMultipart()
message["from"] = "pk"
message["to"] = "mishraprasant66@gmail.com"
message["subject"] = "test"

body = template.substitute({"name" : "Prasant"}) # or name = "PK"
message.attach(MIMEText("Body"))
message.attach(MIMEText(body, "html"))
message.attach(MIMEText("This is the mail body"))
message.attach(MIMEImage(Path(r"C:\Users\Prasant\Desktop\10731005_1603312636564029_7927403856296757991_n.jpg").read_bytes()))

with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
# smtp = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
    smtp.ehlo() # helo msg
    smtp.starttls() # transport layer security, with this all the commands we send will be encrypted
    smtp.login("mishraprasant73@gmail.com", "app_password") # from 
    smtp.send_message(message)
    print("sent...")
# smtp.close()
# generate an app password for this
