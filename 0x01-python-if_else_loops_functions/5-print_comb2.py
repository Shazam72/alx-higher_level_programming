#!/usr/bin/python3
for n in list(range(0, 100)):
    print("{:02d}, ".format(n) if n != 99 else "{:02d}".format(n), end='')
print()
