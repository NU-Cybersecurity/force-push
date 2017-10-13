#!/usr/bin/env python3

import argparse
version = 'Vaporware'

class PARSE(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='FORCEPUSH', description='', add_help=False)
        self.parser.add_argument('-h', '--help', action='help')
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s {v}'.format(v=version))

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
