"""
O(n) time
O(1) space
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res += n & 1
            n >>= 1
        return res