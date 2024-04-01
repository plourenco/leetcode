"""
123. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        trades = []
        # We do not need all past trades for counting
        # memory usage could be optimized
        for i in range(0, k * 2):
            trades.append(0 if i % 2 else prices[0])
        for price in prices:
            trades[0] = min(price, trades[0])
            if price - trades[0] > trades[1]:
                trades[1] = price - trades[0]
            for i in range(2, k * 2, 2):
                if price - trades[i - 1] <= trades[i]:
                    trades[i] = price - trades[i - 1]
                if price - trades[i] > trades[i + 1]:
                    trades[i + 1] = price - trades[i]

        return trades[-1] if k > 0 else 0


print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
print(Solution().maxProfit(4, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))
print(Solution().maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
