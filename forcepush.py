#!/usr/bin/env python3
'''
Forcepush 0.1
Written by: John Galbraith, name, name, name, name



'''

import argparse #Needed to parse arguments
import traceback #Needed for troubleshooting


def main():
    '''
    This is the main file for forcepush where it all comes
    together.
    '''
    print('Hello World')


if '__main__' in __name__:
    try:
        main()
    except:
        print(traceback.format_exc())