import smtplib
import ssl
import csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "strooizout.python@gmail.com" 
receiver_email = "strooizout.python+person1@gmail.com"  
password = 'PythonBot2021' #input("Type your password and press enter: ")

# create multipart message
message = MIMEMultipart()
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email


body = """\
Hi {name},
How are you?
Real Python has many great tutorials:
www.realpython.com
"""

filename = "strooizout.csv"  
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")

message.attach(MIMEText(body, "plain"))
message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for name, receiver_email in reader:
            server.sendmail(sender_email, receiver_email, text.format(name=name))

    # server.sendmail(sender_email, receiver_email, text)