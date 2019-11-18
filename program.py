from tkinter import *
from random import choice


class Santa:
    from_name = ""
    to_name = ""

    def __init__(self):
        self.from_name = self.getName()
        self.to_name = self.getName()

    def cleanCsv(self):
        with open("B2A.csv", 'r') as workfile:
            splited_list = []
            appened_list = []
            for i in workfile:
                splited_list = i.split(';')
                del splited_list[2]
                appened_list.append(splited_list)
            del appened_list[0]
            return appened_list

    def getName(self):
        return choice(self.cleanCsv())

    def setName(self, new_from_name):
        self.from_name = new_from_name


santa1 = Santa()
print(f"{santa1.from_name}\n{santa1.to_name}")

