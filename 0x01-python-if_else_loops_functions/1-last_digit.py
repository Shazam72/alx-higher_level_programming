#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = number % -10
else:
    lastDigit = number % 10
first_part = f"Last digit of {number} is {lastDigit}"
if lastDigit == 0:
    print(first_part, "and is 0")
elif (lastDigit > 5):
    print(first_part, "and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    print(first_part, "and is less than 6 and not 0")
