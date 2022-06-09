#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elm = set(filter(lambda x: x in set_2, set_1))
    diff_elm = (set_1 | set_2) - diff_elm
    return(diff_elm)
