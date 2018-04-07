#------------------------------------------------------------------------------------
# This is a simple script demonstrates the use of Python to send email.
# Written by Leon Wee, April 2018.
# Anyone may freely copy or modify this program.
#------------------------------------------------------------------------------------

import smtplib

TO = ['leonweecs@gmail.com', 'leon-wee@hotmail.com'] # add more email address here to send this email to more people!
SUBJECT = 'Python Class'
TEXT = 'You just sent an email via Python, congratulations!'

# Gmail Sign In
gmail_sender = 'xxxxxx@gmail.com' # put your own email address
gmail_passwd = 'xxxxxx' # put your own email password, please do not share this file or your password to other people

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, TO, BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()