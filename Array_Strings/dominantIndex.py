from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l, l2 = -1, -1
        for e, v in enumerate(nums):
            if l < v:
                l2 = l 
                l = v
                e_store = e
            elif l2 < v:
                l2 = v

        if l >= 2*l2:
            return e_store

        return -1

nums = [1,0]
print(Solution().dominantIndex(nums))