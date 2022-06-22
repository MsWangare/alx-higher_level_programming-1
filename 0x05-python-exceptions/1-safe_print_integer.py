#!/usr/bin/python3

## prints x elements of a list.

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    except TypeError:
        return False
    return True
