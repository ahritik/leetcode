"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""

def searchInsert(nums, target):
    left = 0
    right = len(nums)

    while left < right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid

    return left