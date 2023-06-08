#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    _sum = 0
    _len = len(argv) - 1
    if _len != 0:
        for i in list(range(1, _len + 1)):
            _sum = _sum + int(argv[i])
    print(_sum)
