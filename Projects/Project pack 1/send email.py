# sending email using python

import smtplib

def send_email(to, content):
    # 587 is port number
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # ehlo is smtp command 
    server.ehlo()
    # starters starts the negotiation
    server.starttls()
    # generate passwod from the app
    server.login("your email", "your password")
    #send mail
    server.sendmail("your email", to, content)
    # close the server
    server.close()
    
if __name__ == "__main__":
    try:
        content = input("Type your text: \n ")
        to = input("Whom to send the email: \n")
        send_email(to, content)
        print("email has been sent!")
        
    except Exception as e:
        print(e)
        print("Sorry email not sent")
        
