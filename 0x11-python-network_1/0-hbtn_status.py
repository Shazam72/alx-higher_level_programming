#!/usr/bin/python3
"""Script that fetch https://alx-intranet.hbtn.io/status."""
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as resp:
    data = resp.read()
    print('Body response:')
    print(f"\t- type: {data.__class__}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data.decode()}")
