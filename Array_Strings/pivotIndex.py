from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        prev_v = 0

        for e, v in enumerate(nums):
            l += prev_v
            r -= v
            prev_v = v

            if l == r:
                return e
        return -1


nums = [2,1,-1]
print(Solution().pivotIndex(nums))
