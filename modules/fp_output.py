#!/usr/bin/env python3

import smtplib
import email
import os
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE
import mimetypes
import getpass

class EMAIL(object):
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
        self.server = smtplib.SMTP('smtp.gmail.com:587')


    def buildmail(self, report=''):
        self.mailfrom = 'nobody@nowhere.nope'

        #Build the list of To: addresses
        self.tolist = []
        self.tolist.append('jagalbraith@icloud.com')

        # Build the list of Cc: addresses
        cclist = []
        #cclist.append('jagalbraith@icloud.com')

        # Build the list of Bcc: addresses
        bcclist = []
        #bcclist.append('jagalbraith@icloud.com')

        #Body of the email
        html = '''
        <html><head></head><body>
        <p>
        Here is your report<br />
        {report}
        </body></html>
        '''.format(report=report)

        msg = MIMEMultipart()
        msg['From'] = self.mailfrom
        msg['To'] = COMMASPACE.join(self.tolist)
        msg['Cc'] = COMMASPACE.join(cclist)
        msg['Bcc'] = COMMASPACE.join(bcclist)
        msg['Subject'] = 'FORCEPUSH REPORT'
        msg.attach(MIMEText(html, 'html'))
        self.message = msg
        self.sendmail()


    def sendmail(self):
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.username,self.passwd)
        self.server.sendmail(self.mailfrom, COMMASPACE.join(self.tolist), self.message.as_string())
        self.server.quit()

        
 class OUTPUT(object):
    def __init__(self):
        self.bar = 'hello world'

    def kitten(self, cat):
        print(self.bar)
        return cat



if '__main__' in __name__:
    username = raw_input('Gmail Username:')
    passwd = getpass.getpass()
    mail = EMAIL(username, passwd)
    mail.buildmail(report='Test message')
    
    meowmix = OUTPUT()
    print(meowmix.kitten("meow"))


