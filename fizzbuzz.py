#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: %s count" % sys.argv[0])
    sys.exit(1)

try:
    count = int(sys.argv[1])
except ValueError as e:
    print("argument must be integer")
    sys.exit(1)

for i in range(1, count+1):
    s = ''
    if i % 3 == 0:
        s += 'Fizz'
    if i % 5 == 0:
        s += 'Buzz'

    if not s:
        s += str(i)

    print(s)
