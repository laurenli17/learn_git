from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            day_profit = prices[i] - prices[i - 1]
            if day_profit > 0:
                profit += day_profit

        return profit