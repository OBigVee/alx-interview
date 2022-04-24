#!/usr/bin/env python3


def isEven(n: int) -> bool:
    """Even number checker, returns boolean"""
    checker = True if n % 2 == 0 else False
    return checker


def minOperations(n: int) -> int:
    """returns minimum number of operation"""
    trackOps: int = 0
    leastOps: int = 2
    while n > 1:
        while isEven(n) == True:
            trackOps += leastOps
            n / leastOps
        leastOps += 1
    return trackOps
