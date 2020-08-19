import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(id):
    mail_content = "Your request with ID " + id + " is registered!"
    #The mail addresses and password
    sender_address = 'ppawar@wilp.bits-pilani.ac.in'
    sender_pass = 'Rishi1234'
    receiver_address = 'pravin.pawar@pilani.bits-pilani.ac.in'

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
