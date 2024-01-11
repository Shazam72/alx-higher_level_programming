#!/usr/bin/python3
"""Send request to <URL> and display body with managing errors."""
import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode())
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')
