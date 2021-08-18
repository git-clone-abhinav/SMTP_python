import smtplib
from dotenv import load_dotenv
import os

# Pulling the credentials from the .env file
load_dotenv()
uid = os.getenv('gmail')
passphrase = os.getenv('password')

def send_mail(uid,passphrase,sub,body,mail_to):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(uid,passphrase)
    msg = f"Subject: {sub}\n\n{body}"
    server.sendmail(
        uid,
        mail_to,
        msg
    )
    print("Mail has been Sent !")
    server.quit()

email_ids=[]
n=int(input("How many mails do u wanna send ?"))
for i in range(n):
    email = input(f"Enter email no {i}:")
    email_ids.append(email)

sub = input("Enter Subject for the Mail : ")
body = input("Enter Body of the Mail : ")

for mail_to in email_ids:
    send_mail(uid,passphrase,sub,body,mail_to)