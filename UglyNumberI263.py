"""
263. Ugly Number I

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.
"""

def isUgly(n):
    if not n: return False
    for i in [2,3,5]:
        while n % i == 0: n //= i
    return n == 1