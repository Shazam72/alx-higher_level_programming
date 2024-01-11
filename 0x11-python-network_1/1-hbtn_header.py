#!/usr/bin/python3
"""Script that sequest to an url and display the value of X-Request-Id."""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))
