'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

from collections import Counter

def singleNumber(nums) -> int:
    freq = Counter(nums).items()
    
    for key, val in sorted(freq):
        if val == 1:
            return key