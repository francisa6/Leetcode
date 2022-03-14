from typing import List
from icecream import ic


class Solution:
    """
    Since this binary search doesn't have a target we need to include
    that value into our l, r halves. Here we will include it into 
    the right half. This means we replace our normal r = mid - 1 by r = mid.
    """

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
        mid = (l + r) // 2

        if nums[r] < nums[mid]:
            l = mid + 1
        else:
            r = mid


nums = [15, 17, 11, 13, 14]
print(Solution().findMin(nums))
