#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{:d} {:s}{:s}".format(len(argv) - 1, "argument" if len(argv) < 3 else "arguments",
        "." if len(argv) == 1 else ":"))
    for i, j in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, j))
