#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rev_list = []
    for i in my_list:
        rev_list.append(my_list.pop())
    return rev_list
