#!/usr/bin/env python3

import nmap

import optparse
class SCAN(object):
    def __init__(self):
        self.isopen = '[+] Open Like 7-11 :'


    def scan(self, ip, port, outfile):
        '''this function scans ssh, telnet, ftp, webmin, and returns service information'''
        nmScan = nmap.Scanner()
        nmScan.scan(self, subNet,  '21', '22', '23', '10000')
        targetrange = []
        for host in nmScan.all_hosts(21, 22, 23, 10000):
            if nmScan[host].has_ftp(21):
             state = nmScan[host]['ftp'][21]['state']
             if state == 'open':
                success='{z}{host}:{port}\n'.format(host=host,port='21/ftp', z=self.isopen)
                print(success)
                outfile.append(success)
            if nmScan[host].has_ssh(22):
             state = nmScan[host]['ssh'][22]['state']
             if state == 'open':
                success = '{z}{host}:{port}\n'.format(host=host, port='22/ssh', z=self.isopen)
                print(success)
                outfile.append(success)
            if nmScan[host].has_telnet(23):
             state = nmScan[host]['telnet'][23]['state']
             if state == 'open':
                success = '{z}{host}:{port}\n'.format(host=host, port='23/telnet', z=self.isopen)
                print(success)
                outfile.append(success)
            if nmScan[host].has_webmin(10000):
             state = nmScan[host]['webmin'][10000]['state']
             if state == 'open':
                success = '{z}{host}:{port}\n'.format(host=host, port='10000/webmin', z=self.isopen)
                print(success)
                outfile.append(success)

