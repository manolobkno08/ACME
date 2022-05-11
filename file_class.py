#!/usr/bin/env python3

"""
Class file - Singleton Pattern

"""


def singleton(cls):
    """Set only one instance using the singleton pattern"""
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrap


@singleton
class File(object):
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
            c = [i for i in f if i != "\n"]
            # print(c)
            if len(c) < 5:
                return False
            else:
                return True

    def save_to_dictionary(self):
        """Save data into new dictionary"""
        new_dic = {}
        with open(self.__path_file, "r", encoding="utf-8") as f:
            for line in f:
                user, values = line.strip().split("=")
                new_dic[user] = values
        return new_dic

    def convert_hours(self, new):
        """Split hours and storage as"""
        for key, value in new.items():
            hours = value.split("-")
            newlist = []
            for hour in hours:  # [10:00, 12:00]
                res = hour.split(":")
                x = list(map(int, res))
                newlist.append(x)
            hours = newlist  # [[10, 0], [12, 0]]

            for i in range(len(hours)):
                hour = hours[i][0]
                minute = hours[i][1]
                hour_decimal = hour + (minute / 60.0)
                hours[i] = hour_decimal
            new[key] = hours

    def data_dict_to_dict(self, new_dict):
        """Convert to dictionary of dictionaries"""
        for key, value in new_dict.items():
            new = {}
            hours = value.split(",")
            for item in hours:
                new[item[:2]] = item[2:]
            self.convert_hours(new)
            new_dict[key] = new

        return new_dict

    def final_comparison(self, final_dict):
        """Method that return a final comparison between employees"""
        final = {}

        visited = []
        for user1, days1 in final_dict.items():
            visited.append(user1)
            for user2, days2 in final_dict.items():
                if user2 not in visited:
                    common_days = days1.keys() & days2.keys()
                    count = 0
                    for day in common_days:
                        start_user1, end_user1 = days1[day]
                        start_user2, end_user2 = days2[day]
                        if start_user2 > end_user1:
                            continue
                        elif end_user2 < start_user1:
                            continue
                        else:
                            count += 1
                    if count > 0:
                        key = user1 + "-" + user2
                        final[key] = count
        return final
