#!/usr/bin/python3
"""Fetches at https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == '__main__':
    with requests.get('https://alx-intranet.hbtn.io/status') as resp:
        data = resp.content.decode()
        print('Body response')
        print(f"\t- type: {data.__class__}")
        print(f"\t- content: {data}")
