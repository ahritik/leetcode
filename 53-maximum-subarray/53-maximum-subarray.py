class Solution(object):
    def maxSubArray(self, nums):
        maxSub = -1000000
        rSum = 0

        for num in nums:
          rSum += num
          maxSub = max(maxSub, rSum)
          rSum = max(rSum, 0)

        return maxSub
        