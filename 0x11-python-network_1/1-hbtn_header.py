#!/usr/bin/python3
"""Script that sequest to an url and display the value of X-Request-Id."""
import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as resp:
    print(dict(resp.headers).get('X-Request-Id'))
