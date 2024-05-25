#!/usr/bin/env python3


def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    a, b = 0, 1
    result = []
    for _ in range(length):
        result.append(a)
        a, b = b, a + b

    print(result)
























