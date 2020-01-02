import smtplib
#import subprocess

class Account:
    def __init__(self, us, pw = ""):
        self.us = us
        self.pw = pw

Accounts = []
CurrentAccount = None

def emailCMD (subject, body, toM):
    #USES CONF SETTINGS, NOT CURRENT ACCOUNT
    
    # ("echo " + '"' + body + '" | mail -s "' + subject + '" ' + toM)
    pass

def email (subject, body, toM):
    header = "To: " + toM + "\n" + "From: " + CurrentAccount.us + "\n" + "Subject: " + subject
    
    
    s = smtplib.SMTP("smtp.gmail.com", 587)

    s.ehlo()
    s.startls()
    s.ehlo()

    s.login(CurrentAccount.us, CurrentAccount.pw)
    s.sendmail(CurrentAccount.us, toM, header + "\n\n" + body)

    s.quit()
