class Solution(object):
    def maxProfit(self, prices):
        left = 0
        max_profit = 0

        while left < len(prices):
            right = len(prices) - 1
            while left < right:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
                right -= 1

            left += 1
        return max_profit


# Todo
# Fix time exceed for large input
# 198/202 passed
