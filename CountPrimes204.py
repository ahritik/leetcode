'''
204. Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.
'''

from math import sqrt

def countPrimes(n):
    if n < 3: return 0
    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2,sqrt(n)+1):
        if primes[i]:
            for j in range(i+i, n, i): primes[j]=False

    return primes.count(True)