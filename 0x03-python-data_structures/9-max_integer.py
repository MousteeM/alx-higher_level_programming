#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        for i in my_list:
            if my_list[i] > my_list[0]:
                my_list[i] = my_list[0]
        return my_list[i]
