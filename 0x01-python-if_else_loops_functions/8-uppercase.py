#!/usr/bin/python3
def uppercase(str):
    for c in str:
        _c = ord(c)
        is_lower = 97 <= _c <= 123
        print("{:c}".format(_c - 32) if is_lower else "{}".format(c), end="")
    print()
