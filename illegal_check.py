#!/usr/bin/env python

import os
import requests
import sys
import re

keywords = ['apple', 'banana', 'orange']

def keyword_match(keywords, text):
    pattern = "|".join(keywords)
    matches = re.findall(pattern, text)

    return matches

def do_illegal_check(text):
    try:
        #text = 'I have an apple and a banana'

        matches = keyword_match(keywords, text)
        return matches

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file, 'r') as f:
        text = f.read()
    print(do_illegal_check(text))

    f.close()

