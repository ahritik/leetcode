"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.
"""

def isPowerOfTwo(n):
    if n == 1:
        return True
    elif n==0:
        return False
    elif n % 2 != 0:
        return False
    else:
        return isPowerOfTwo(n/2)