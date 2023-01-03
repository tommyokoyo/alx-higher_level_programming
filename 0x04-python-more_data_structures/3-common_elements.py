#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for item in set_1:
        if item in set_2:
            my_list.append(item)
    return my_list
# return(set_1 & set_2)
