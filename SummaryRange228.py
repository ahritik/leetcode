'''
228. Summary Ranges
Easy

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b
'''

def summaryRanges(nums):
    ans = []

    i = 0
    while i < len(nums):
        begin = nums[i]
        while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
            i += 1
        ans.append(str(begin))

        if begin != nums[i]:
            ans[-1]+= "->" + str(nums[i])

        i += 1

    return ans

print("Input: range = [0,1,2,4,5,7]   Output:",summaryRanges([0,1,2,4,5,7]))
print("Input: range = [0,2,3,4,6,8,9] Output:",summaryRanges([0,2,3,4,6,8,9]))
print("Input: range = []              Output:",summaryRanges([]))