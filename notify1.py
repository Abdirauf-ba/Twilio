#!/usr/bin/env python
# Install the Python helper library from twilio.com/docs/python/install

from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(ACCOUNT_SID, AUTH_TOKEN)
binding = client.notify.services('jfkljdljflkja;ljfkljsalk;j') \
    .bindings.create(
        # We recommend using a GUID or other anonymized identifier for Identity
        identity='0001',
        binding_type='sms',
        address='<number>')
print(binding.sid)
