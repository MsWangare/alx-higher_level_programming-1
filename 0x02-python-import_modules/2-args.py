#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv) - 1
    if ln == 0:
        print("{} arguments.".format(ln))
    elif ln == 1:
        print("{} argument:".format(ln))
    else:
        print("{} arguments:".format(ln))
    for i in range(ln):
        print("{}: {}".format(i + 1, argv[i + 1]))
        i + 1
