from typing import List
from icecream import ic


class Solution:
    """
    Since this binary search doesn't have a target we need to include
    that value into our l, r halves. Here we will include it into 
    the right half. This means we replace our normal r = mid - 1 by r = mid.
    """

    def findMax(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if l < mid and nums[mid] > nums[r]:
                l = mid
            elif l <= mid and nums[r] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]


nums = [10, 11, 17]
nums = [20, 21, 27, 18]
# nums = [11, 17, 10]
print(Solution().findMax(nums))
