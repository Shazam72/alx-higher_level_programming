#!/usr/bin/python3
"""Takes your github credentials and displays your id using gith api."""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
