from typing import List

# Time complexity is (uniqueNums * |nums|) approx. O(|nums|)
# Space complex. is O(|uniqueNums|)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        return 2*sum(uniqueNums) - sum(nums)

    def singleNumberXOR(self, nums: List[int]) -> int:
        # A number x^x = 0 and 0^y = y. This means that all of the dups will 
        # cancel out. Also it is important to note that XOR is commutative! 
        # So we can easily visualise that the cancellation process.
        # https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/discuss/43000/Python-different-solutions.?page=2
        res = 0
        for n in nums:
            res ^= n
        return res