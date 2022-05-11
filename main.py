#!/usr/bin/env python3

"""
Console

"""

from modules.read_file import clear, read_file


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
                        clear()
                        read_file(username)
                        break

                    elif choise == 2:
                        run = False
                        print(f"\n\t=>  See you later {username}!\n")

                    elif choise < 0 or choise != 1 or choise != 2:
                        clear()
                        print("\t=>  Option not valid")

                except ValueError:
                    clear()
                    print("\t=>  The option must be a number")
            else:
                clear()
                username = input(
                    "\t=>  User not valid, enter your username again: ").upper()
        else:
            clear()
            username = input(
                "\t=>  Please, enter your username again: ").upper()


if __name__ == "__main__":
    """
    Initiallize main loop
    """
    ACMECommand()
