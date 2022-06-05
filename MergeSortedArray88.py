'''
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

def mergeSorted(nums1, m, nums2, n):
    m -= 1
    n -= 1
    maxLen = m + n - 1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[maxLen] = nums1[m]
            maxLen -= 1
            m -= 1
        else:
            nums1[maxLen] = nums2[n]
            n -= 1
            maxLen -= 1
    while n >= 0:
        nums1[maxLen] = nums2[n]
        n -= 1
        maxLen -= 1

    return nums1

print("Input: [1,2,3,0,0,0], 3, [2,5,6], 3  Output:",mergeSorted([1,2,3,0,0,0], 3, [2,5,6], 3))
print("Input: [1], 1, [], 0  Output:",mergeSorted([1], 1, [], 0))