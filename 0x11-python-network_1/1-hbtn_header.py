#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.

Usage: .//1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
