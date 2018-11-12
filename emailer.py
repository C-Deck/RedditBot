from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Class to store the email
class email:
    def __init__(self, body, subject, post):
        self.body = body
        self.subject = subject
        self.post = post

#Sends an email to proper email
def sendEmail(email):
    msg = MIMEMultipart()
    msg['From'] = "DeckerRedditBot@gmail.com"
    msg['To'] = "cdecker18@gmail.com"
    msg['Subject'] = "Submission Found"

    msg.attach(MIMEText(email.body, 'html'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['From'], "Hidden") #Password will be added later
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()