import smtplib as sm
from email.message import EmailMessage

def mail_send(maildetail):
    msg=EmailMessage()
    msg["from"]=maildetail[0]
    msg["to"]=maildetail[1]
    msg["subject"]="this is the sample program with attacment"
    msg.set_content("mail with attachment!!!")
    fp=open("logged.txt","rb")
    data=fp.read()
    msg.add_attachment(data,maintype="text",subtype="octet-stream",filename="log.txt")
    mail=sm.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login(maildetail[0],maildetail[1])
    # body="helooo"
    try:
        mail.sendmail(maildetail[0],maildetail[2],msg.as_string())
        print("msg sent")
    except:
        print("error occured")
    mail.quit()
    return


