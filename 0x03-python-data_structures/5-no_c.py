#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) > 0:
        string = ''
        for char in my_string:
            if char != 'c' and char != 'C':
                string += char
        return(string)
    else:
        return(my_string)
