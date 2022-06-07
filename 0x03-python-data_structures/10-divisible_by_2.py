#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_mult = []
    for i in my_list:
        is_mult.append(True) if i % 2 == 0 else is_mult.append(False)
    return(is_mult)
