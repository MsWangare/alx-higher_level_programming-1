#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > -1 and idx < len(my_list):
        while(idx < len(my_list)):
            return(my_list[idx])
    else:
        return(None)
