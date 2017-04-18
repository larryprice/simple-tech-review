#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: %s count" % sys.argv[0])
    sys.exit(1)

try:
    count = int(sys.argv[1])
except ValueError as e:
    print("count argument must be int")
    sys.exit(1)

def factorial(num):
    if num == 0 or num == 1:
        return 1

    return num*factorial(num-1)

print(factorial(count))
