"""
2160. Minimum Sum of Four Digit Number

You are given a positive integer num consisting of exactly four digits. 
Split num into two new integers new1 and new2 by using the digits found in num. 
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
"""

def minSum(num):
    numList = sorted([int(i) for i in str(num).strip("")])
    return (10*numList[0]+numList[2]) + (10*numList[1]+numList[3])
