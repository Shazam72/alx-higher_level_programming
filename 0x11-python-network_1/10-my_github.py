#!/usr/bin/python3
"""Takes your github credentials and displays your id using gith api."""
import requests
import sys

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f"Bearer {sys.argv[2]}",
    'X-GitHub-Api-Version': '2022-11-28'
}
url = "https://api.github.com/user"
with requests.get(url, headers=headers) as resp:
    try:
        if resp.status_code != 200:
            print(None)
        else:
            data = resp.json()
            print(data['id'])
    except KeyError:
        print(None)
