import smtplib
from email.mime.text import MIMEText

sender = "pythonapp@zoznam.sk"
sender_psw = "AppPython123"
receivers = ""


port = 587
msg = MIMEText("msg")

msg["Subject"] = "Subject"
msg["From"] = sender
msg["To"] = receivers

with smtplib.SMTP("smtp.zoznam.sk", port) as server:

    server.login(user=sender, password=sender_psw)

    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")
