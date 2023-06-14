#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    if roman_string is None or type(roman_string) != str:
        return value
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
            letter_val = values[roman_string[i]]
            if i > 0 and letter_val > values[roman_string[i - 1]]:
                value += letter_val - 2*values[roman_string[i - 1]]
            else:
                value += letter_val
        return value
    except KeyError:
        return 0
