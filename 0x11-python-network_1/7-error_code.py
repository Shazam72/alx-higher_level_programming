#!/usr/bin/python3
"""Send request to <URL> and display body with managing errors."""
import sys
import requests

if __name__ == '__main__':
    with requests.get(sys.argv[1]) as resp:
        if resp.status_code in [200]:
            print(resp.content.decode())
        else:
            print(f'Error code: {resp.status_code}')
