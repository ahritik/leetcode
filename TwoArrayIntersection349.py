'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
'''

def arrayIntersection(nums1, nums2):
    return set(nums1) & set(nums2)