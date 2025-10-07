class Solution(object):
    def maxProfit(self, prices):
        i = 0
        max_profit = 0
        while i < len(prices):
            max_profit = max(max_profit, (max(prices[i : len(prices)]) - prices[i]))
            i += 1
        return max_profit
