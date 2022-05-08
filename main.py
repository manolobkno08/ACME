#!/usr/bin/env python3

"""
Console

"""
import sys
import os


def ACMECommand():
    """
    Start program

    """
    run = True

    while run:
        try:
            choise = int(input("""
            ==== Welcome to ACME ====
            Please choose your option:

            1      Read file
            2      Exit

            Your option: """))

            if choise < 0 or choise != 1 or choise != 2:
                os.system("clear")
                print("\t=>  Option not valid")

            if choise == 1:
                os.system("clear")
                print("\t=>  SELECT FILE")

            if choise == 2:
                run = False
                os.system("clear")
                print("\t=>  See you soon!\n")
        except ValueError:
            os.system("clear")
            print("\t=>  The option must be a number")


# Read files from arguments
# file = sys.argv[1]
# print(file)

if __name__ == "__main__":
    """
    Initiallize main loop
    """
    ACMECommand()
