"""
O(n) for the first and O(nlogn) time for last 2 solutions
O(1) space
"""

from typing import List

# when there are only two distinct elements 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        c = 0
        for n in nums:
            if candidate == n:
               c += 1
            elif c == 0:
                candidate, c = n, 1
            else:
                c -= 1
        return candidate



class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        

# General solution for when there are more than 2 
# distinct elements
class GeneralSolution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        c = 0
        prev_v = nums[0]
        for v in nums:  
            if v != prev_v:
                c = 0
                prev_v = v
            c += 1
            if c > int(len(nums) / 2):
                return v