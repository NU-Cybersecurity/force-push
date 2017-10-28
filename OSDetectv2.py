#!/usr/bin/env python3

import nmap
import getpass

host = '127.0.0.1'

if 'root' in getpass.getuser():
    n = nmap.PortScanner()
    n.scan(host, arguments='-sT -O')
    if 'osclass' in n[host]:
        for opt in n[host]['osclass']:
            print(opt)
    else:
        print('Unable to determine OS.')

