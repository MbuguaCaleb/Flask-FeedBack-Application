import smtplib 
from email.mime.text import MIMEText #helps you use HTML from within your mail


def send_mail(customer, dealer,rating,comments):
    port = 2525
    smpt_server ='smtp.mailtrap.io'
    login ='8e3dfb641d4aa4'
    password='18775361aee01b'
    message =f"<h3>New feedback Submission</h3><ul><li>Customer:{customer}</li><li>Dealer:{dealer}</li><li>Rating:{rating}</li><li>Commets:{comments}</li><ul>"


    sender_email ='mbuguacaleb30@gmail.com'
    receiver_email='caleb@wizglobal.co.ke'
    msg = MIMEText(message,'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To']= receiver_email

    #send email
    with smtplib.SMTP(smpt_server, port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())




 



