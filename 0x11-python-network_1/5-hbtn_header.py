#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import sys
import requests


def main():
    """ X-Request -Id"""
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
