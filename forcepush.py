#!/usr/bin/env python3
'''
Forcepush 0.1
Written by: John Galbraith, Jodee Lowe, Branson Hutchens, Sean Poojaroen, Bradley Petrini, Geoff Collier



'''

import modules.fp_args
import traceback #Needed for troubleshooting

#In the main we give a brief rundown of what the tol is designed for and what modules we plan on writting to make this a suite and not just a tool
def main():
    '''
    This is the main file for forcepush where it all comes
    together.
    '''
    # 1. Check account and make sure super user.
    ###Local code
    ### Ask for output email address if not specified in cmd line

    # 2. Get the arguments.
    argmod = modules.fp_args.PARSE()
    arguments = argmod.args()
    print(arguments)

    # 3. Determine red or blue
    ### Local Code # Update here

    # 4. Determine output and set up report file
    ### Local code if email, Call fp_output.py if stdout

    ### Red
    # Run NMAP module
    ###Call fp_scan.py

    ### Blue
    # Run the monitor mode module
    ### Call fp_monitor.py

    # 5. If --attack
    ### Call fp_attack.py

    # 6. If email send email.
    ### Call fp_output.py


if '__main__' in __name__:
    try:
        main()
    except SystemExit:
        print('So.... Do you feel like a hacker now?\n')
    except:
        ### Call fp_output.py and send error email.
        print(traceback.format_exc())