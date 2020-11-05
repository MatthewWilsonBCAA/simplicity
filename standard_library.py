import random
import re

def repr_float(x):
    try:
        x = int(x)
        return True
    except:
        return False

oper_list = ["+", "-", "/", "*"]

class standard_f():
    def __init__(self, info):
        info = info
        self.vars = {}

    def pr(self, text):
        print(text)

    def inp_f(self):
        return input()

    def var_f(self, var):
        self.vars[var[0]] = var[1]

class express():
    #example: (5 + 5), (2 - 3)
    def __init__(self, initial):
        self.initial = initial
    
    def split_it(self):
        #re.split(" ||", info)
        info = list(self.initial)
        self.left = ""
        self.right = ""
        self.op = ""
        seen_left = False
        for i in info:
            if repr_float(i):
                if seen_left:
                    self.right += i
                else:
                    self.left += i
            elif i in oper_list:
                self.op = i
                seen_left = True
    def solve(self):
        if repr_float(self.left):
            l = float(self.left)
        else:
            l = self.left.solve()
        if repr_float(self.right):
            r = float(self.right)
        else:
            r = self.right.solve()
        if self.op == "+":
            return l + r
        elif self.op == "-":
            return l - r
        elif self.op == "/":
            return l / r
        elif self.op == "*":
            return l * r

        # print("Wh-" + self.left + " " + self.op + " " + self.right)
        
new_expression = express("15 + 2")
new_expression.split_it()
print(new_expression.solve())
    