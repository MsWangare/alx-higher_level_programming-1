#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to
the URL and displays
the value of the X-Request-Id variable found in the header of
the response.
"""
import sys
from urllib.request import urlopen


def main():
    """ sends a request to the url"""
    url = sys.argv[1]
    with urlopen(url) as response:
        print(response.headers['X-Request-Id'])


if __name__ == "__main__":
    main()
