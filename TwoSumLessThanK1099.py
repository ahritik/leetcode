'''
1099. Two Sum Less Than K

Given an array nums of integers and integer k, return the maximum sum such that there exists 
i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.
'''

def twoSumLessThanK(nums, k):
    nums.sort()
    front = 0
    back = len(nums) - 1
    sumk = -1
    while front < back:
        if nums[front] + nums[back] < k:
            sumk = max(sumk, nums[front] + nums[back])
            front += 1
        else:
            back -= 1

    return sumk