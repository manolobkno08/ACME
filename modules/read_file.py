#!/usr/bin/env python3

"""
Read File Verification

"""
import time
import os
from classes.file import File


def clear():
    """Method that clear data from the console"""
    return os.system("clear")


def get_path_files(choose_file):
    """Get absolute path to read files"""
    separator = os.path.sep
    path = os.path.dirname(os.path.realpath(__file__))
    r = separator.join(path.split(separator)[:-1])
    path_file = f"{r}{separator}files{separator}{choose_file}"
    return path_file


def read_file(username):
    """Method that allow verify and read txt files"""
    choose_file = input("""
                        ===== Read File - ACME =====
                        Please, enter the name of the file:

                        Usage:      filename.txt\n
                        Enter filename: """)

    path_file = get_path_files(choose_file)

    # CHECK SINGLETON PATTERN
    # newFile = File()
    # newFile2 = File()
    # print(newFile is newFile2)

    # New object instance
    newFile = File()
    flag = 0
    newFile.path_file = path_file

    try:
        if not newFile.verify_txt():
            flag = 2
            raise Exception()

        if not newFile.verify_content():
            flag = 1
            raise Exception()

        new_dict = newFile.save_to_dictionary()
        final_dict = newFile.data_dict_to_dict(new_dict)
        final_result = newFile.final_comparison(final_dict)

        clear()
        print("""
                        ===== Final Report - ACME =====
                        Pairs of employees who have coincided in the office.
                        """)

        [print(f"\t\t\t{key}: {value}") for key, value in final_result.items()]

        print(f"\n\t=>  See you later {username}!\n")
        time.sleep(1.5)
        exit()

    except Exception:
        if flag == 1:
            print("\n\t=>  File '{x}' must contain at least five sets of data".
                  format(x=choose_file))
        elif flag == 2:
            print(
                f"\n\t=>  File must be .txt")
        else:
            print(f"\n\t=>  File '{choose_file}' not found")

        choise = input("\n\t\t\tWould you like to continue? (y/n): ")

        if choise == "y":
            clear()
            read_file(username)
        elif choise == "n":
            clear()
            print(f"\n\t=>  See you later {username}!\n")
            time.sleep(1.5)
            exit()
        else:
            clear()
            print(f"\n\t=>  Option not valid\n")
            choise = input("\n\t\t\tWould you like to continue? (y/n): ")
            clear()
            read_file(username)
