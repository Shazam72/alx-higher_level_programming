#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    _len = len(argv) - 1
    print(f"{_len} arguments" if _len != 1 else f"{_len} argument", end="")
    print(":" if _len > 0 else ".")
    for el in argv:
        if argv.index(el) == 0:
            continue
        print("{}: {}".format(argv.index(el), el))
