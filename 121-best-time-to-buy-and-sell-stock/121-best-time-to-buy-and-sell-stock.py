class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = 0
        hold = -10000000

        for price in prices:
          sell = max(sell, hold + price)
          hold = max(hold, -price)

        return sell