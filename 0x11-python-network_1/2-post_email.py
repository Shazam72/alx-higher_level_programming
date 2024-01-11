#!/usr/bin/python3
"""Send an email to <URL> using post with <email> as parameter."""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as resp:
        print(resp.read().decode())
