#!/usr/bin/python3

"""function returns a list of lists of integers representing the
Pascal's triangle of n"""


def factorial(n):
    """Function computes the factorial of any number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def pascal_triangle(n):
    """returns an empty list if n<= 0
    assumes n will always be an integer
    """
    num = []
    if not isinstance(n, int):
        return "n need to be an int"
    elif(n <= 0 ):
        return num
    else:
        for i in range(n):
            for j in range(n - 1):
                print(end="")
            for j in range(i + 1):
                val = factorial(i) // (factorial(j) * factorial(i - j))
        num.append(val)
    return(num)
