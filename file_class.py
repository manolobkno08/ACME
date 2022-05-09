#!/usr/bin/env python3

"""
Class file

"""


class File():
    """
    Initialization of File class
    """

    def __init__(self, path_file):
        """
        Constructor method
        """
        self.__path_file = path_file

    def verify_txt(self):
        """Method that verify if the file is a txt file"""
        r = self.__path_file.split(".")
        if r[1] == "txt":
            return True
        else:
            return False

    def verify_content(self):
        """Verify if the file contains at least five lines"""
        with open(self.__path_file, "r", encoding="utf-8") as f:
            c = [i for i in f.readlines()]
            if len(c) < 5:
                return False
            else:
                return True
