#!/usr/bin/env python3

class COLOR(object):
    def __init__(self):
        pass

    #This designates the various colors chosen to make the help module more fun to read and easier to differentiate between the various fields
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

    def printfh(self):
        bar = '\n' + '-' * 50
        header = "Force-Push Fancy Help"
        print(COLOR.bold + COLOR.underline + header + COLOR.end)
        print(bar)

        '''Help Files'''
        #This is the argument that will be designated to pull up the help file
        stdhelp = '{c} -h, --help : Standard help file. {e}'.format(c=COLOR.blue, e=COLOR.end)
        print(stdhelp)
        fancyhelp = '{c} -fh, --fancyhelp {e}: {c2}Fancy help file. {e}'.format(c=COLOR.green, c2=COLOR.lmagenta, e=COLOR.end)
        print(fancyhelp)
        print(bar)

        ''' EMAIL OUTPUT'''
        #This shows the various ways to output the results.  If no email is designated stdout will default
        definition = "--Emails reports using GMail for SMTP--"
        print(definition)

        dashe = "-e  : Email address of the recipient"
        print(COLOR.red + dashe + COLOR.end)

        dashgu = "-gu : GMail username for the sender's mailbox"
        print(COLOR.red + dashgu + COLOR.end)

        dashgp = "-gp : GMail password for the sender's mailbox"
        print(COLOR.red + dashgp + COLOR.end)



if '__main__' in __name__:
    test = OUTPUT()
    test.printfh()
