#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for a in range(list_length):
        try:
            if type(my_list_1[a] or my_list_2[a]) == (int or float):
                result_list.append(my_list_1[a] / my_list_2[a])
        except TypeError:
            print("wrong type")
            result_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            a += 1
    return result_list
