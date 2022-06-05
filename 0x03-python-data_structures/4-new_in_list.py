#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list2 = my_list.copy()
    if idx > -1 and idx < len(my_list2):
        my_list2[idx] = element
        return(my_list2)
    else:
        my_list2 = my_list
        return(my_list2)
