#!/usr/bin/python3
#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
from urllib import request


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            print(response.headers['X-Request-Id'])
