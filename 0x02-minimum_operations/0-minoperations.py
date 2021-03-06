#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    '''function calculates the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    trackOPerations = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            trackOPerations += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            trackOPerations += 2
        elif clipboard > 0:
            done += clipboard
            trackOPerations += 1

    return trackOPerations
