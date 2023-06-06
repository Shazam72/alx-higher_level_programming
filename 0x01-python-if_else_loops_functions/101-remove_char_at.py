#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ''
    str_len = len(str)
    for i in list(range(0, str_len)):
        if i == n:
            continue
        str2 = str2 + str[i]
    return str2
