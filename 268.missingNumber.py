"""
O(n) time 
O(1) space
"""
from typing import List

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)


