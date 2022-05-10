#!/usr/bin/env python3

"""
Read File Verification

"""
import time
import os
from file_class import File


def clear():
    """Method that clear data from the console"""
    return os.system("clear")


def read_file(username):
    """Method that allow verify and read txt files"""
    choose_file = input("""
                        ==== Read File - ACME ====
                        Please, enter the name of the file:

                        Usage:      filename.txt\n
                        Enter filename: """)

    # Get absolute path to the file
    path_file = os.path.dirname(os.path.realpath(
        __file__)) + "/files/" + choose_file

    # New object instance
    newFile = File(path_file)
    flag = 0

    try:
        if not newFile.verify_txt():
            raise Exception()

        # if not newFile.verify_content():
        #     flag = 1
        #     raise Exception()

        new_dict = newFile.save_to_dictionary()
        # print(new_dict)

        print(newFile.data_representation(new_dict))
        # with open(path_file, "r", encoding="utf-8") as f:
        #     print(f.read(), end="")

    except Exception:
        if flag == 1:
            print(
                f"\n\t=>  File '{choose_file}' must contain at least five lines")
        else:
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
