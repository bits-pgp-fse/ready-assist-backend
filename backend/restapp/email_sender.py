import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Refer https://www.tutorialspoint.com/python/python_sending_email.htm

def send_email(id):
    mail_content = "Your request with ID " + id + " is registered!"
    #The mail addresses and password
    sender_address = <Update EMAIL ID here>
    sender_pass = <Update EMAIL password here>
    receiver_address = <Update EMAIL ID here>

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
