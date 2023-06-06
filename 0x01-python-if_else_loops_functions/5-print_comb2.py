#!/usr/bin/python3
for n in list(range(0, 100)):
    print(f"{n:02d}, " if n != 99 else f"{n:02d}", end='')
print()
