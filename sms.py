# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC04cd39d30875af9538b76b8970649cc7"
auth_token = '09eff29012754bc6a76c8cf8f05361d3'
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+12525422390",
  to="+50766158599"
)
print(message.sid)


