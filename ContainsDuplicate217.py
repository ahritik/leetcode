'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

def containsDuplicate(nums:int):
    return len(nums) != len(set(nums))

