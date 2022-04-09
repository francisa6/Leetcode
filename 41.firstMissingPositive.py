"""
O(n) time
O(1) space
"""
from typing import List


class Solution:
    # O(n) time and O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        for j in range(len(nums)):
            while 0 < nums[j] <= len(nums) and nums[nums[j] - 1] != nums[j]:
                nums[nums[j] - 1], nums[j] = nums[j], nums[nums[j] - 1]

        i = 1
        j = 0
        while j < len(nums) and nums[j] <= i:
            if nums[j] == i:
                i += 1
            j += 1
        return i


class SolutionLong:
    # O(nlogn) time and O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        i = 1
        j = 0
        while j < len(nums) and nums[j] <= i:

            if nums[j] == i:
                i += 1

            j += 1

        return i
