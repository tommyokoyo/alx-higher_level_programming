#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    lst = 0
    for a in range(x):
        try:
            if type(a) == int:
                print("{:d}".format(my_list[a]), end="")
                lst += 1
            else:
                continue
        except (TypeError, ValueError):
            continue
    print("")
    return lst
