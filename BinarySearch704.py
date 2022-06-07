'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
'''

def binarySearch(target, nums) -> int:
    if nums.length == 0:
        return -1

    start = 0
    end = len(nums)

    while start < end:
        mid = ((end-start) // 2) + start
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid+1

    return -1

print("Input:[-1,0,3,5,9,12], 9   Output:",binarySearch([-1,0,3,5,9,12],9))
print("Input:[-1,0,3,5,9,12], 2   Output:",binarySearch([-1,0,3,5,9,12],2))