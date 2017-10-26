#!/usr/bin/env python3

class COLOR(object):
    def __init__(self):
        pass
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    inverted = '\033[7m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    lgray = '\033[37m'
    dgray = '\033[90m'
    lred = '\033[91m'
    lgreen = '\033[92m'
    lyellow = '\033[93m'
    lblue = '\033[94m'
    lmagenta = '\033[95m'
    lcyan = '\033[96m'
    white = '\033[97m'
    bgdefault = '\033[49m'
    bgblack = '\033[40m'
    bgred = '\033[41m'
    bggreen = '\033[42m'
    bgyellow = '\033[43m'
    bgblue = '\033[44m'
    bgmagenta = '\033[45m'
    bgcyan = '\033[46m'
    bglgray = '\033[47m'
    bgdgray = '\033[100m'
    bglred = '\033[101m'
    bglgreen = '\033[102m'
    bglyellow = '\033[103m'
    bglblue = '\033[104m'
    bglmagenta = '\033[105m'
    bglcyan = '\033[106m'
    bgwhite = '\033[107m'

class OUTPUT(object):
    def __init__(self):
        pass
    header = "FP_Output Help"
    definition = "--Emails reports using GMail for SMTP--"
    dashe = "-e  : Email address of the recipient"
    dashgu = "-gu : GMail username for the sender's mailbox"
    dashgp = "-gp : GMail password for the sender's mailbox"


if '__main__' in __name__:
    print COLOR.bold + COLOR.underline + OUTPUT.header + COLOR.end
    print OUTPUT.definition
    print COLOR.red + OUTPUT.dashe
    print OUTPUT.dashgu
    print OUTPUT.dashgp + COLOR.end
