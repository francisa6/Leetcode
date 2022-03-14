from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif (
                (target >= nums[l] and target < nums[mid])
                or (nums[mid] < nums[l] <= target)
                or (target < nums[mid] < nums[l])
            ):
                r = mid - 1
            else:
                l = mid + 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 7
print(Solution().search(nums, target))
