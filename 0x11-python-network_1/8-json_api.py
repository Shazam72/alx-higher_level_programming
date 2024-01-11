#!/usr/bin/python3
"""Requests JSON depending on <letter>."""
import requests
import sys

if __name__ == '__main__':
    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1] if len(q) == 1 else ''
    data = {'q': q}
    with requests.post('http://0.0.0.0:5000/search_user', data) as resp:
        try:
            json = resp.json()
            print(f"[{json['id']}] {json['name']}")
        except KeyError:
            print('No result')
        except ValueError:
            print('Not a valid JSON')
