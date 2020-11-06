import standard_library as std

def repr_float(x):
    try:
        x = int(x)
        return True
    except:
        return False

objects = {}
variables = {}
with open("new_main.sp") as file:
    while True:
        com = file.readline()
        x = com.split(":")
        x.reverse()
        z = 0
        is_comment = False
        for i in x:
            if "c//" in i:
                is_comment = True
                break
            if "=" in i:
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
                exper = objects[i][1].strip()
                if (std.oper_list[0] in exper or std.oper_list[1] in exper or std.oper_list[2] in exper or std.oper_list[3] in exper) and not "'" in exper:
                    for var in variables:
                        if var in exper:
                            exper = exper.replace(var, variables[var])
                    exper = str(std.express(exper).solve())
                if exper == "g_in":
                    exper = input("[user]")
                variables[objects[i][0].strip()] = exper
            if "g_exp" in i:
                working = i.replace("g_exp", "")
                working = str(int(working) + 1)
                if objects["g_pr" + working] == objects[i].initial:
                    objects["g_pr" + working] = objects[i].solve()
            elif "g_pr" in i:
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
            elif "g_end" in i:
                exit()
        x = []
        objects = {}