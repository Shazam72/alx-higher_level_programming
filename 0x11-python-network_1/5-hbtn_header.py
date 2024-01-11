#!/usr/bin/python3
"""Script that sequest to an url and display the value of X-Request-Id."""
import requests
import sys

if __name__ == '__main__':
    with requests.get(sys.argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))
