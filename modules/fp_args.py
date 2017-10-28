#!/usr/bin/env python3

import argparse
version = '.1'
#This is the module we used to designate the arguments for the various modules so the user will have to get comfortable running from CLI since this is designed as a tool for beginners
class PARSE(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='FORCEPUSH', description='', add_help=False)
        self.parser.add_argument('-h', '--help', action='help')
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s {v}'.format(v=version))
        self.parser.add_argument('-e', '--email', help='Email address to send report to.')
        self.parser.add_argument('-gu', '--gmailuser', help='Gmail Username')
        self.parser.add_argument('-gp', '--gmailpasswd', help='Gmail Password')



    def args(self):
        self.args = self.parser.parse_args()
        dictionary = vars(self.args)
        arguments = {}
        for key in dictionary.keys():
            if dictionary[key]:
                arguments[key] = dictionary[key]
        return arguments


if '__main__' in __name__:
    ga = PARSE()
    args = ga.args()
    print(args)
