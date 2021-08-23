import smtplib
from dotenv import load_dotenv
import os
from logger import log_it
# Pulling the credentials from the .env file
load_dotenv()
uid = os.getenv('gmail')
passphrase = os.getenv('password')

def send_mail(uid,passphrase,sub,body,mail_to):
    try:
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
        print(f"Mail sent to {mail_to}".format())
        server.quit()
        sub = "test" #input("Enter Subject for the Mail : ")
        body = "test" #input("Enter Body of the Mail : ")
        mail_id = "abhi.anu003@gmail.com"
        send_mail("uid",passphrase,sub,body,mail_id)
        log_it(1000,f"Mail sent to {mail_id} with subject = {sub} and body = {body}".format())
    except Exception as e:
        error_code =  e.smtp_code
        error_message = e.smtp_error
        print("Exception Raised : ", e)
        print("Error Code : ", error_code)
        print("Error Message : ", error_message)