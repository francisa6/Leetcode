"""
O(n) time and O(1) space
You're allowed to buy and sell the stock on the same day given that you 
only hold one unit of the stock at any 1 point in time 
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        profit = 0
        for p in prices[1:]:
            if b < p:
                profit += p - b
            b = p
        return profit

