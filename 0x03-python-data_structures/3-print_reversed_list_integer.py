#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_range = len(my_list) - 1
    for i in my_list:
        if i >= 0:
            print("{:d}".format(i))
            i = i - 1
