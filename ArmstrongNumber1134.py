"""
1134. Armstrong Number

Given an integer n, return true if and only if it is an Armstrong number.
The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.
"""

from math import pow

def isArmstrong(n):
    return n == sum([pow(int(i),len(str(n))) for i in str(n)])
