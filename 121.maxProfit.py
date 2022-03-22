class Solution:
    """
    O(n) time
    """

    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        highest_profit = 0
        for price in prices[1:]:
            highest_profit = max(highest_profit, price - lowest_price)
            lowest_price = min(lowest_price, price)
        return highest_profit


class Solution:
    """
    naive sol that is O(n^2) time
    """

    def maxProfit(self, prices: List[int]) -> int:
        def profit(b, bp):
            currV = 0
            for sp in prices[b + 1 :]:
                v = sp - bp
                if v > currV:
                    currV = v
            return currV

        currP = -1
        for b, bp in enumerate(prices[:-1]):
            currV = profit(b, bp)
            if currV > currP:
                currP = currV

        return currP if currP > 0 else 0
