#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (my_list):
        my_list2 = my_list
        if idx > -1 and idx < len(my_list2):
            my_list2[idx] = element
            return(my_list2)
    else:
        return(my_list2)
