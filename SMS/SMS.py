from twilio.rest import Client

account_sid = 'aa234dfafad24525243sf'
auth_token = 'fg457sdhdhde435rer'
client = Client(account_sid, auth_token)

message = client.messages.create(
                from_ = '9876543210',
                body = 'Hello, \n Sample Message, Please ignore! ',
                to = '9876543210'
            )

print(message.sid)
