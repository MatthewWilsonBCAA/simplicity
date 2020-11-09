c// Welcome to Simplicity!

c// this is a comment
c// g_ is used to denote a built-in keyword DO NOT USE
c// g_pr: is used to print whatever text is on the other side of the colon
g_pr:Hello World!


c// variable assignments can have math inside them!
firvar = 3 + 3
secvar = 3


total = (firvar + secvar) / (2)

c// the % symbol is used to denote when you want to use a variable's value

g_pr:The average of %firvar% and %secvar% is %total%.
g_pr:What is your name?
name = g_in
g_pr:welcome back, matt!

g_pr:%name% is cool!
g_pr:could you give me two numbers, pressing enter between each?
x = g_in
y = g_in
total = x + y
g_pr:the total is %total%

c// required for the program to end
c// if you dont, the intepreter will keep going into oblivion!
g_end