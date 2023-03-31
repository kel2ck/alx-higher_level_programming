#!/usr/bin/python3
"""Fetches a header of a response from a URL."""
from urllib.request import urlopen, Request
import sys

if __name__ == "__main__":
    req = Request(sys.argv[1])
    with urlopen(req) as resp:
        print(resp.getheader('X-Request-Id'))
