"""
2006. Count Number of Pairs With Absolute Difference K

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
The value of |x| is defined as:
    x if x >= 0.
    -x if x < 0.
 
"""

def countKDifference(nums, k):
    count = 0
    
    for i in set(nums):
        count += nums.count(i)*nums.count(i+k) + nums.count(i)*nums.count(i-k)
        nums = [j for j in nums if j != i]
    """
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            count += 1 if abs(nums[i]-nums[j])==k else 0
    """
    return count
    