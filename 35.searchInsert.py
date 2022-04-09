"""
O(n) time
O(1) space
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for e, v in enumerate(nums):
            if v >= target:
                return e
            
        return len(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l

nums = [1,1]
target = 2

print(Solution().searchInsert(nums, target))