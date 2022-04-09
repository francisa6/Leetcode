"""
O(n) time and O(1) space
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        curr_val = nums[l]
        for r in nums[1:]:
            if curr_val != r:
                nums[l+1] = r
                l += 1
                curr_val = nums[l]
        return l + 1


# nums = [1, 2, 6, 1, 6]
# [0]
# [1, 1, 1]
# [1, 1, 2, 6, 6]
nums = [1, 2, 6, 1, 6]
print(Solution2().removeDuplicates(nums))
print(Solution2().removeDuplicates(nums) == len(set(nums)))

