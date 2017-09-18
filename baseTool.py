#!/usr/bin/env python

from sys import argv, exit
import base64

def exitWithError():
    print(f"Usage: base64.py option({'|'.join(options)}) argument")
    exit(1)

options = ['e', 'encode', 'd', 'decode']

if len(argv) != 3:
    exitWithError()

option = argv[1].strip()
arg = argv[2].strip()

if not argv[1].strip() in options:
    print(f"Invalid option: ${option}".strip())
    exitWithError()

if option in ['e', 'encode']:
    print(base64.b64encode(bytes(arg,  "utf-8")).decode('utf-8'))
elif option in ['d', 'decode']:
    print(base64.b64decode(arg).decode('utf-8'))
else:
    print(f'Not implemented option: ${option}')
