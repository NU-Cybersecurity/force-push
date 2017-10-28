#!/usr/bin/env python3

import nmap
import getpass

class OSDETECT(object):
    def __init__(self):
        pass


    def osscan(self, host):
        if 'root' in getpass.getuser():
            n = nmap.PortScanner()
            n.scan(host, arguments='-sT -O')
            if 'osclass' in n[host]:
                for opt in n[host]['osclass']:
                    return opt
            else:
                return 'Unable to determine OS.'
        else:
            return 'You must run as ROOT for the os scan option.'


if '__main__' in __name__:
    odt = OSDETECT()
    print(odt.osscan('127.0.0.1'))