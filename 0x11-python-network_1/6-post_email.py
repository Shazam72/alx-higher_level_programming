#!/usr/bin/python3
"""Send an email to <URL> using post with <email> as parameter."""
import requests
import sys

if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    with requests.post(sys.argv[1], data) as resp:
        print(resp.content.decode())
