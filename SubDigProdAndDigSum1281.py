"""
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""

def subtractProductAndSum(self, n: int) -> int:
    numProd, numSum = 1,0
    while n > 0:
        i = n%10
        numProd *= i
        numSum += i
        n//=10
    return numProd-numSum