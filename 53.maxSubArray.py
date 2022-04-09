class Solution:
    """
    we can look at partial sums instead and use the code we wrote from 
    maxProfit question. 
    """

    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        highest_profit = -99999999999999999
        for price in prices[1:]:
            highest_profit = max(highest_profit, price - lowest_price)
            lowest_price = min(lowest_price, price)
        return highest_profit

    def maxSubArray(self, nums: List[int]) -> int:
        partialSums = [0]
        for x in nums:
            partialSums.append(partialSums[-1] + x)
        return self.maxProfit(partialSums)


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)



# class SolutionDC:
#     def maxSubArray(self, nums: List[int]) -> int: