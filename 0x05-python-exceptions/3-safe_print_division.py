#!/usr/bin/python3
def safe_print_division(a, b):
    v = 0
    try:
        v = a / b
    except (ZeroDivisionError, TypeError):
        v = None
    finally:
        print("Inside result: {}".format(v))
    return v
