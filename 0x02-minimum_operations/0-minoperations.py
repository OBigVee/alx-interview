#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given a
number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H=>Copy All=>Paste=>HH=>Paste=>HHH=>Copy All=>Paste=>HHHHHH=>Paste=>HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """method calculates the fewest number of operations
    needed to result in exactly n H character in the file
    """
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
