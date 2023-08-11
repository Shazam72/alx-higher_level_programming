#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
        }
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    res = ops[op](a, b)
    print("{} {} {} = {}".format(a, op, b, res))
