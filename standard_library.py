import random
import re

def repr_float(x):
    try:
        x = int(x)
        return True
    except:
        return False

def repr_str(x):
    try:
        if 'f' in x:
            pass
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

class printable():
    def __init__(self, text):
        self.text = text

    def pr(self):
        print(self.text)

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
        seen_paren = False
        for i in info:
            if repr_float(i) or '(' in i or ')' in i:
                if i == '(':
                    seen_paren = True
                elif i == ')':
                    seen_paren = False

                if seen_left:
                    self.right += i
                else:
                    self.left += i
            elif i in oper_list and seen_paren == False:
                self.op = i
                seen_left = True
            elif i in oper_list and seen_paren == True:
                if seen_left:
                    self.right += i
                else:
                    self.left += i
            
            if repr_str(self.left) and '(' in self.left and ')' in self.left:
                self.left = self.left.replace('(', " ")
                self.left = self.left.replace(')', " ")
                self.left = express(self.left)
            if repr_str(self.right) and '(' in self.right and ')' in self.right:
                self.right = self.right.replace('(', " ")
                self.right = self.right.replace(')', " ")
                self.right = express(self.right) 
    def solve(self):
        self.split_it()
        if repr_float(self.left) == True:
            l = float(self.left)
        else:
            l = self.left.solve()
        if repr_float(self.right) == True:
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
        

f = standard_f('This is the basic function object')
# new_expression = express("(15 + 2) - (5 - 2)")
# print(new_expression.solve())
    