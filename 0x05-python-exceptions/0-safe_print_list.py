#!usr/bin/python3

## prints x elements of a list.

def safe_print_list(my_list=[], x=0):
        j = 0
        try:
            for i in range(x):
                print(my_list[i], end="")
                j += 1
        except IndexError:
            print()
            return j
        print()
        return j
