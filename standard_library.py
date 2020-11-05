import random

class standard_f():
    def __init__(self, info):
        self.info = info
        self.vars = []

    def pr(self, text):
        print(text)

    def inp_f(self):
        return input()

    def var_f(self, var):
        self.vars.append(var)