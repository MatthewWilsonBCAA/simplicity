def repr_float(x):
    try:
        x = int(x)
        return True
    except:
        return False

NEXT_ELSE_EXECUTE = False
NEXT_BLOCK_EXECUTE = False
SEEN_ELSE = False

with open("main.sp") as file:
    while True:
        com = file.readline()
        if NEXT_ELSE_EXECUTE == True:
            if not "else->" in com and not "->\n" == com:
                continue
            else:
                NEXT_ELSE_EXECUTE = False
        if NEXT_BLOCK_EXECUTE == True:
            if not "->\n" == com:
                if "else->" in com:
                    SEEN_ELSE = True
                if SEEN_ELSE == True:
                    continue
            else:
                SEEN_ELSE = False
                NEXT_BLOCK_EXECUTE = False
        if "g_use(f)" in com:
            from standard_library import standard_f
            f = standard_f("This will the basic 'library' for simplicity")
        elif "com>>>" in com:
            continue
        elif "if(" in com:
            com = com.replace("if(", "")
            com = com.replace(")->\n", "", 1)
            tokens = com.split("=")
            for i in f.vars:
                if i[0] in tokens:
                    ind = tokens.index(i[0])
                    tokens[ind] = i[1]
            if tokens[0] + "\n" == tokens[1]:
                NEXT_BLOCK_EXECUTE = True
            else:
                NEXT_ELSE_EXECUTE = True
        elif "f.pr(" in com:
            com = com.replace("f.pr(", "")
            com = com.replace(")", "", 1)
            tokens = com.split("%")
            tokens[-1].replace("\n", "")
            final = tokens[0]
            try:
                for i in f.vars:
                    if i[0] in tokens:
                        ind = tokens.index(i[0])
                        tokens[ind] = str(i[1])
                f.pr(''.join(tokens))
            except:
                print("Error: f not imported, cannot print")
        elif " f.=" in com:
            tokens = com.split(" f.=", 1)
            tokens[1] = tokens[1].strip()
            if "f.inp()" in tokens[1]:
                tokens[1] = f.inp_f()
            else:
                is_num = repr_float(tokens[1])
                if is_num == True:
                    tokens[1] = float(tokens[1])
            try:
                f.var_f(tokens)
            except:
                print("Error: f not imported, cannot define")
        elif "g_end" in com:
            break
    # print("Ended")
