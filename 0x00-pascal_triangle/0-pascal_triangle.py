#!/usr/bin/python3

"""function returns a list of lists of integers representing the
Pascal's triangle of n"""


from logging import raiseExceptions


def factorial(n):
    """Function computes the factorial of ank number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

# def pascal_triangle(n):
#     num = [[1]]
#     compute_n =[]
#     if not isinstance(n,int):
#         raiseExceptions("n is not an int")
#     elif (n < 0):
#         return num
#     else:
#         for i in range(n+1):
#             compute_ = ""
#             for j in range(i-1):
#                 #compute_ =""
#                 compute_ = [combination(i,j) for j in range(i+1) ]
#            #print(compute_n,end = " ".format(int(compute_n)))
#             # for j in range(i+1):
#             #     compute_n = list(combination(i,j))
#             num.append(compute_)
#     return num
    
def pascal_triangle(n):
    assert type(n) == int
    if n <= 0:
        return []
    return [[1]] + [
        [combination(n, k) for k in range(n+1)]
        for n in range(1, n)
    ]