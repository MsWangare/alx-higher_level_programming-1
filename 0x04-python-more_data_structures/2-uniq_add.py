#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = 0
    for i in set(my_list):
        uniq_int += i
        return uniq_int
