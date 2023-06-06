#!/usr/bin/python3
for i in list(range(0, 10)):
    for j in list(range(i + 1, 10)):
        print(f"{i}{j}, " if i != 8 else f"{i}{j}", end="")
print()
