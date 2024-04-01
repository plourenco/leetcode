"""
123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Bonus follow-up: Find the prices for each transaction
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_sale_1 = 0
        min_hold = prices[0]
        max_sale_2 = 0
        for price in prices:
            min_buy = min(price, min_buy)
            if price - min_buy > max_sale_1:
                max_sale_1 = price - min_buy
            if price - max_sale_1 <= min_hold:
                min_hold = price - max_sale_1
            if price - min_hold > max_sale_2:
                max_sale_2 = price - min_hold

        return max_sale_2

    def maxProfit_trades(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_sale_1 = 0
        min_hold = prices[0]
        max_sale_2 = 0
        trades = [None, None, None, None]
        for price in prices:
            min_buy = min(price, min_buy)
            if price - min_buy > max_sale_1:
                trades[0] = min_buy
                max_sale_1 = price - min_buy
            if price - max_sale_1 <= min_hold:
                min_hold = price - max_sale_1
                trades[1] = trades[0] + max_sale_1
                trades[2] = price
            if price - min_hold > max_sale_2:
                max_sale_2 = price - min_hold
                trades[3] = price

        print(
            f'Total: {max_sale_2} with trades: {trades}')
        return max_sale_2


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([1, 1, 7, 0, 0, 3, 5]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
