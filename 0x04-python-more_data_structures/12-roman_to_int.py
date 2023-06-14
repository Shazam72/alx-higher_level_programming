#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    try:
        values = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                }
        for i in range(0, len(roman_string)):
            if i > 0 and values[roman_string[i]] > values[roman_string[i - 1]]:
                value += values[roman_string[i]] - 2 * values[roman_string[i]]
            else:
                value += values[roman_string[i]]
        return value if value > 0 else -value
    except KeyError:
        return 0
