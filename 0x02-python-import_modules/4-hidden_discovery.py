#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as n
    for i in dir(n):
        if i[0] != '_' and i[1] != '_':
            print(i)
