#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    uniq_int = []

    for i in my_list:
        if i not in uniq_int:
            uniq_int.append(i)
            add += i
    return(add)
