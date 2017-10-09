#!/usr/bin/env python3
'''
Module written by: John Galbraith
8 Oct 2017

'''

import traceback


class MAIL(object):
    def __init__(self):
        pass


    def format_email(self):
        pass


    def send_email(self):
        pass


def main():
    mail = MAIL()
    mail.format_email()
    mail.send_email()


if '__main__' in __name__:
    try:
        main()
    except:
        print(traceback.format_exc())