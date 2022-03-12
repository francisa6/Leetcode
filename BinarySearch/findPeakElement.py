from typing import List

"""
Would be neat to extend nums[-1] and nums[n] with -inf but this is expensive to do for non-linked lists as we need to create
a new array using up more memory.

If we allowed for dups next to each other then this would take linear time! becuase we can no longer discard half as we'd be 
checking the next time, next next time, etc. that we'd have a different value.
"""


class Solution:
    """
    O(log(n)) time and O(1) space. Without needing to resize array.
    """

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while True:
            mid = l + (r - l) // 2
            below_mid = nums[mid - 1] if mid > 0 else -(2 ** 31) - 1
            above_mid = nums[mid + 1] if mid < len(nums) - 1 else -(2 ** 31) - 1

            if below_mid < nums[mid] and above_mid < nums[mid]:
                return mid
            elif nums[mid] < above_mid:
                l = mid
            else:
                r = mid


nums = [1, 2, 1, 3]
print(Solution().findPeakElement(nums))


class Solution2:
    """
    O(log(n)) time and O(1) space. Without needing to resize array. Only two cases and using r as last index. 
    """

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l


nums = [1, 2, 4, 3]
print(Solution().findPeakElement(nums))
