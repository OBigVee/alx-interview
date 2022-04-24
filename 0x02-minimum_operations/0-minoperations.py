#!/usr/bin/python3
import time


def isEven(n: int) -> int:
    """Even number checker, returns boolean"""
    if n % 2 == 0:
        checker = True
    else:
        checker = False
    return checker


def minOperations(n: int) -> int:
    """returns minimum number of operation"""
    # print("check the value of n: n = {}".format(str(n)))
    trackOps: int = 0
    leastOps: int = 2
    # s = time.perf_counter()
    # print("Computation started in ----- {} time -------".format(str(s)))
    while n > 1:
        while n % leastOps == 0:
            # while isEven(n):
            #     if n==1:
            #         continue
            trackOps += leastOps
            n //= leastOps
            # else:
            # #if  isEven(n):
            #     trackOps += leastOps
            #     n //= leastOps
            # print("n={} div by leastOps={}:: Equals {}".format(str(n),str(leastOps),str(n)))
        # else:
        # #     continue
        #     print("n == {}.".format(str(n)))
        #     time.sleep(10)
        # print("end Inner While LOOP -> back to Outter LOOP")
        leastOps += 1
    # elapsed = time.perf_counter() - s
    # print("minOpstakes ------- {} time to compute -------".format(str(elapsed)))
    # print(trackOps)
    return trackOps
