import standard_library as std

def repr_float(x):
    try:
        x = int(x)
        return True
    except:
        return False

def g_pr(i):
    try:
        if "%" in objects[i]:
            list_string = objects[i].split("%")
            for var in variables:
                for i in list_string:
                    z = list_string.index(i)
                    i = i.strip()
                    if i == var:
                        list_string[z] = variables[var] 
            print(''.join(list_string))
        else:
            print(objects[i])
    except:             
        print(objects[i])
def g_asg(i):
    exper = objects[i][1].strip()
    if (std.oper_list[0] in exper or std.oper_list[1] in exper or std.oper_list[2] in exper or std.oper_list[3] in exper) and not "'" in exper:
        for var in variables:
            if var in exper:
                exper = exper.replace(var, variables[var])
        exper = str(std.express(exper).solve())
    if exper == "g_in":
        exper = input("")
    variables[objects[i][0].strip()] = exper

def g_exp(i):
    working = i.replace("g_exp", "")
    working = str(int(working) + 1)
    if objects["g_pr" + working] == objects[i].initial:
         objects["g_pr" + working] = objects[i].solve()

objects = {}
blocks = {} # if this works right, this *should* allow me to store blocks of codes into
#a dictionary of lists, then execute later
in_block = ''
use_block = None
block_count = 0
variables = {}

with open("new_main.sp") as file:
    while True:
        if in_block == '':
            com = file.readline()
            x = com.split(":")
            x.reverse()
        else:
            x = use_block
        z = 0
        is_comment = False
        for i in x:
            if "c//" in i:
                is_comment = True
                break
            if "g_if" in i:
                objects["g_if" + str(z)] = x
                blocks["g_if" + str(z)] = x
                block_count += 1
            if "=" in i and not "==" in i:
                new_var = i.split("=")
                # for var in variables:
                #     for temp in new_var:
                #         ind = variables.index(var)
                #         temp = temp.strip()
                #         if temp == var:
                objects["g_asg" + str(z)] = new_var
                # variables[new_var[0]] = new_var[1]
            elif "g_pr" in i:
                objects["g_pr" + str(z)] = x[z - 1]
            elif (std.oper_list[0] in i or std.oper_list[1] in i or std.oper_list[2] in i or std.oper_list[3] in i) and not "'" in i:
                ind = x.index(i)
                result = i
                for var in variables:
                    if var in result:
                        result = result.replace(var, variables[var])
                        x[ind] = result
                objects["g_exp" + str(z)] = std.express(result)
            elif "g_end" in i:
                objects["g_end"] = 1
            z += 1


        for i in objects:
            if is_comment == True:
                break
            if "g_asg" in i:
                g_asg(i)
            # if "g_if" in i:
            #     use_block = blocks[i]
            #     print(use_block)
            #     # in_block = 
            if "g_exp" in i:
                g_exp(i)
            elif "g_pr" in i:
                g_pr(i)
            elif "g_end" in i:
                exit()
                
        x = []
        objects = {}