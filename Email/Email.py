import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Test Email'
email['to'] = 'test@test.com'
email['subject'] = 'This is Test Email'     # Subject of email
email.set_content('I am the Python Master. \n This is Test Email, \n Please ignore!!')      # Body of Email

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('test.email@gmail.com', 'abctestabc')  # Login to the Email Account
    smtp.send_message(email)

print('Done.....')

