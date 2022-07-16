'''
349. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''


def arrayIntersection(nums1, nums2):
    counts = {}
    intersection = []

    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    for num in nums2:
        if num in counts and counts[num] > 0:
            intersection.append(num)
            counts[num] -= 1

    return intersection