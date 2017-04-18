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

def fibonacci(num):
    if num <= 1:
        return 1

    return fibonacci(num-1) + fibonacci(num-2)

def fib_loop(num):
    a, b = 1, 1
    for i in range(0, count+1):
        print(a)
        a, b = b, a + b

# for i in range(0, count+1):
#     print(fibonacci(i))

fib_loop(count)
