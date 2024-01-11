#!/usr/bin/python3
"""Fetches at https://alx-intranet.hbtn.io/status."""
import requests

resp = requests.get('https://alx-intranet.hbtn.io/status')
data = resp.content.decode()
print('Body response')
print(f"\t- type: {data.__class__}")
print(f"\t- content: {data}")
