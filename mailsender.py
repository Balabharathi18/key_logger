import smtplib as sm
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail_send(mail1_ID,passwd,rec_mail):
    mail=sm.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login(mail1_ID,passwd)
    body="file attachment"
    try:
        mail.sendmail(mail1_ID,rec_mail,body)
        print("msg sent")
    except:
        print("error occured")
    mail.quit()
    return
# mail_send(mail_ID,passwd,rec_mail)


