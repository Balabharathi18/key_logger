from mailsender import mail_send


def generator():
    mail_ID=input("enter the sender mailid:")
    passwd=input("enter the sender's password:")
    rec_mail=input("Enter the reciever's mail:")
    mail_send(mail_ID,passwd,rec_mail)
    return
generator()
