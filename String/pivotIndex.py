# O(1) space and O(N) time

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums) 
        for i, n in enumerate(nums):
            right_sum = right_sum - n

            if left_sum == right_sum:
                return i
                
            left_sum = left_sum + n

        return -1        