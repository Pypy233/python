import smtplib
from email.mime.text import MIMEText
msg = MIMEText('The body of the email is here')
msg['Subject'] = 'An Email Alert'
msg['From'] = '2529716798@qq.com'
msg['To'] = '2529716798@qq.com'
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit