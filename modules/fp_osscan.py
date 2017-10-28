#!/usr/bin/env python3

#Importing the modules we'll need
import nmap
import getpass

#Defining our class and function
class OSDETECT(object):
    def __init__(self):
        pass

#Using nmap to scan for the host OS
    def osscan(self, host):
        if 'root' in getpass.getuser():         #Must be looged in as a root user or use sudo
            n = nmap.PortScanner()
            n.scan(host, arguments='-sT -O')    #Adding arguments to the scan to get the target OS
            if 'osclass' in n[host]:
                for opt in n[host]['osclass']:
                    return opt                 
            else:                              #Incase nmap was unable to determine the OS
                return 'Unable to determine OS.'
        else:                                  #Incase the user isn't root or using sudo
            return 'You must run as ROOT for the os scan option.'


if '__main__' in __name__:
    odt = OSDETECT()
    print(odt.osscan('127.0.0.1'))              #Display the OS found by the scan
