#!/usr/bin/env python3

"""
Class file

"""
import time
import os


class File():
    """
    Initialization of File class
    """

    def __init__(self, filename, username):
        """
        Constructor method
        """
        self.__filename = filename
        self.__username = username
