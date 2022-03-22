# O(N) time and O(1) space

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        smallerMax, maxval = -100, -100

        for i, n in enumerate(nums):
            if n > maxval:
                maxindex = i
                smallerMax, maxval = maxval, n
            else: 
                smallerMax = max(smallerMax, n)
        
        if smallerMax * 2 <= maxval:
            return maxindex

        return -1