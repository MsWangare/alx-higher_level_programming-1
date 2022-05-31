#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = repr(number)
num = num[-1]
num = int(num)
if number < 0:
    num *= -1

str1 = "and is less than 6 and not 0"
str2 = "and is greater than 5"

if num < 6 and num != 0:
    print("Last digit of {:d} is {:d} {:s}".format(number, num, str1))
elif num == 0:
    print("Last digit of {:d} is 0 and is 0".format(number))
else:
    print("Last digit of {:d} is {:d} {:s}".format(number, num, str2))
