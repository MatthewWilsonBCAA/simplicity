import standard_library as std

def repr_float(x):
    try:
        x = int(x)
        return True
    except:
        return False

with open("new_main.sp") as file:
    while True:
        com = file.readline()
        if "<comment>" in com:
            continue
        elif "g_end" in com:
            break