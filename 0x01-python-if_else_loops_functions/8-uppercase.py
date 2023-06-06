#!/usr/bin/python3
def uppercase(stringer):
    for c in stringer:
        _c = ord(c)
        print(f"{_c - 32:c}" if 97 <= _c <= 123 else f"{c}", end="")
    print()
