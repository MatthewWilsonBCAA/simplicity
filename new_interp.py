import standard_library as std

def repr_float(x):
    try:
        x = int(x)
        return True
    except:
        return False

objects = {}
with open("new_main.sp") as file:
    while True:
        com = file.readline()
        x = com.split(":")
        x.reverse()
        z = 0
        for i in x:
            if "g_pr" in i:
                objects["g_pr" + str(z)] = x[z - 1]
                z += 1
            elif (std.oper_list[0] in i or std.oper_list[1] in i or std.oper_list[2] in i or std.oper_list[3] in i) and not "'" in std.oper_list:
                objects["g_exp" + str(z)] = std.express(i)
                z += 1
            elif "g_end" in i:
                objects["g_end"] = 1
                z += 1
            else:
                z += 1
        for i in objects:
            if "g_exp" in i:
                working = i.replace("g_exp", "")
                working = str(int(working) + 1)
                if objects["g_pr" + working] == objects[i].initial:
                    objects["g_pr" + working] = objects[i].solve()
            elif "g_pr" in i:
                print(objects[i])
            elif "g_end" in i:
                exit()
        objects = {}



        # if "<comment>" in com:
        #     continue
        # if "g_solve" in com:
        #     x.remove("g_solve")
        #     i = std.express(x[-2]).solve()

        # if "g_pr(" in x:
        #     x.remove("g_pr(")
        #     x.remove(")\n")
        #     std.f.pr(x)
            
        # elif "g_end" in x:
        #     break