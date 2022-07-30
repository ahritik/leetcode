"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
"""

def countBits(n):
    return [str(bin(i)).count("1") for i in range(n+1)]