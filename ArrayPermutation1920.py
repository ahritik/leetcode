'''
1920. Build Array from Permutation

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
'''
def arrayPermutation(nums):
    n = len(nums)

    for i, num in enumerate(nums):
        nums[i] += n * (nums[num] % n)

    for i in range(n):
        nums[i] //= n

    return nums

print("Input: [0,2,1,5,3,4]  Output:",arrayPermutation([0,2,1,5,3,4]))
print("Input: [5,0,1,2,3,4]  Output:",arrayPermutation([5,0,1,2,3,4]))