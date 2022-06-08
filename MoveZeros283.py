'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
This must be done this in-place without making a copy of the array.
'''

def moveZeroes(nums):
    nZPointer = 0
    for num in nums:
        if num != 0:
            nums[nZPointer] = num
            nZPointer += 1

    for i in range(nZPointer, len(nums)):
        nums[i] = 0

