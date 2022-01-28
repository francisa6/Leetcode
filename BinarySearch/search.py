from typing import List
from icecream import ic


class Solution:
    """
    Requires reparameterisation into new coordinates
    """

    def search(self, nums: List[int], target: int) -> int:
        j, shift_right = nums[0], 0
        while shift_right < len(nums) and nums[shift_right] >= j:
            shift_right += 1

        l, r = 0, len(nums) - 1
        while l <= r:
            old_mid = (l + r) // 2
            mid = (old_mid + shift_right) % len(nums)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = old_mid + 1
            else:
                r = old_mid - 1
        return -1


nums = [4, 5, 6]
target = 6
print(Solution().search(nums, target))
