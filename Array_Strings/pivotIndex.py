from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)

        for e, v in enumerate(nums):
            l += v
            if l == r:
                return e
            r -= v
        return -1


nums = [2,1,-1]
print(Solution().pivotIndex(nums))
