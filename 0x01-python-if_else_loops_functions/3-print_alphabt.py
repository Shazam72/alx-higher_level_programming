#!/usr/bin/python3
for c in list(range(97, 97+26)):
    if c != 97 + 16 and c != 97 + 4:
        print("{:c}".format(c), end='')
