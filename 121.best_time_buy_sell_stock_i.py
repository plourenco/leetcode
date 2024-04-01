"""
121. Best Time to Buy and Sell Stock I
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-i
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit


print(Solution().maxProfit([7, 6, 4, 3, 1]))
