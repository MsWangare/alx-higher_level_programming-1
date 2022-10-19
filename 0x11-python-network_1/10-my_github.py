#!/usr/bin/python3
"""
- Python script that takes your GitHub credentials
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    """ main"""
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))


if __name__ == "__main__":
    main()
