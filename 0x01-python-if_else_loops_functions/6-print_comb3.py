#!/usr/bin/python3

for nmbr in range(0, 9):
    for i in range(nmbr + 1, 10):
        if nmbr == 8 and i == 9:
            print("{:d}{:d}".format(nmbr, i))
        else:
            print("{:d}{:d}".format(nmbr, i), end=", ")
