#!/usr/bin/env python3

"""
Console

"""
import time
import os


def read_file(username):
    """Method that allows to read a specific file."""
    choose_file = input("""
                        ==== Read File - ACME ====
                        Please, enter the name of the file:

                        Usage:      filename.txt\n
                        Enter filename: """)
    try:
        with open(choose_file, "r", encoding="utf-8") as f:
            print(f.read(), end="")
    except Exception:
        print(f"\n\t=>  File '{choose_file}' not found")
        choise = input("\n\t\t\tWould you like to continue? (y/n): ")
        if choise == "y":
            os.system("clear")
            read_file()
        elif choise == "n":
            os.system("clear")
            print(f"\n\t=>  See you later {username}!\n")
            time.sleep(2)
            exit()


def ACMECommand():
    """
    Start program menu

    """
    run = True
    username = input("\t=>  Enter your username: ").upper()

    while run:
        if len(username) > 0:
            if username.isspace() == False:
                try:
                    choise = int(input(f"""
                        ==== ¡{username}! Welcome to ACME ====
                        Please, choose one of the following options:

                        1      Read file
                        2      Exit

                        Your option: """))

                    if choise == 1:
                        os.system("clear")
                        read_file(username)

                    elif choise == 2:
                        run = False
                        print(f"\n\t=>  See you later {username}!\n")

                    elif choise < 0 or choise != 1 or choise != 2:
                        os.system("clear")
                        print("\t=>  Option not valid")

                except ValueError:
                    os.system("clear")
                    print("\t=>  The option must be a number")
            else:
                os.system("clear")
                username = input(
                    "\t=>  User not valid, enter your username again: ").upper()
        else:
            os.system("clear")
            username = input(
                "\t=>  Please, enter your username again: ").upper()


if __name__ == "__main__":
    """
    Initiallize main loop
    """
    ACMECommand()
