#!/usr/bin/env python3

"""
Read File Verification

"""
import time
import os


def clear():
    """Method that clear data from the console"""
    return os.system("clear")


def verify_txt(path_file):
    """Method that verify if the file is a txt file"""
    r = path_file.split(".")
    if r[1] == "txt":
        return True
    else:
        return False


def read_file(username):
    """Method that allow verify and read txt files"""
    choose_file = input("""
                        ==== Read File - ACME ====
                        Please, enter the name of the file:

                        Usage:      filename.txt\n
                        Enter filename: """)

    path_file = os.path.dirname(os.path.realpath(
        __file__)) + "/files/" + choose_file

    try:
        if not verify_txt(path_file):
            raise Exception()

        with open(path_file, "r", encoding="utf-8") as f:
            print(f.read(), end="")

    except Exception:
        print(f"\n\t=>  File '{choose_file}' not found [must be .txt]")
        choise = input("\n\t\t\tWould you like to continue? (y/n): ")
        if choise == "y":
            clear()
            read_file(username)
        elif choise == "n":
            clear()
            print(f"\n\t=>  See you later {username}!\n")
            time.sleep(2)
            exit()
        else:
            clear()
            print(f"\n\t=>  Option not valid\n")
            choise = input("\n\t\t\tWould you like to continue? (y/n): ")
            clear()
            read_file(username)
