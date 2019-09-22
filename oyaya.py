import os
from twilio.rest import Client

account = os.environ.get('TWILIO_ACCOUNT_SID')
token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account, token)
#num=['+254712360234','+254712171225']
num = open('/home/ali/contacts.txt','r').readlines()

#num.readline()
#for i in range(0,len(num)):
#      message = client.messages.create(num[i], from_=os.environ.get('TWILIO_PHONE_NUMBER'),
#            body="Hello ")
for number in num:
    message = client.messages.create(
        to=number,
        #from_="JKUMSA WAAYE",
        #from_=os.environ.get('TWILIO_PHONE_NUMBER'),
        messaging_service_sid=os.environ.get('MESSAGING_SERVICE_ID'),
        body=""" YOUR MESSAGE HRE""")
    print(message.sid)
