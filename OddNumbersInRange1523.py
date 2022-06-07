'''
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''

def countOdds(low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2