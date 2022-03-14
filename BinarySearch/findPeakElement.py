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


nums = [1, 2, 1, 3, 5, 6, 4]
print(Solution().findPeakElement(nums))


class Solution2:
    """
    O(log(n)) time and O(1) space. Without needing to resize array. Only two cases and using r as last index. 
    Select Array interpretation: selected range indexed by l, r inclusively are possible values of the peak!
    """

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                # is not r = mid - 1 because if we have nums = [5, 6, 4], mid = 1, l = 0, r = 2 then we wouldn't be excluding 6!
                r = mid

        return l


nums = [1, 2, 1, 3, 5, 6, 4]
print(Solution2().findPeakElement(nums))


class RecursiveSolution:
    """
    O(log(n)) time and O(1) space. Without needing to resize array. Only two cases and using r as last index. 
    Select Array interpretation: selected range indexed by l, r inclusively are possible values of the peak!
    """

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        def sub(l, r):

            if l == r:
                return l

            mid = l + (r - l) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                # is not r = mid - 1 because if we have nums = [5, 6, 4], mid = 1, l = 0, r = 2 then we wouldn't be excluding 6!
                r = mid

            return sub(l, r)

        return sub(l, r)


nums = [5]
# nums = [5, 6]
# nums = [6, 4]
# nums = [5, 6, 4]
# nums = [6, 5, 4]
# nums = [4, 5, 6]
# nums = [4, 5, 6, 2]
# nums = [1, 2, 1, 3, 5, 6, 4]
print(RecursiveSolution().findPeakElement(nums))

