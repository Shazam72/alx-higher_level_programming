#!/usr/bin/python3
for c in list(reversed(range(65, 65+26))):
    print("{:c}".format(c+32) if c % 2 == 0 else "{:c}".format(c), end='')
