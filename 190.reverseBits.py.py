"""
O(n) time
O(1) space 
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += ((n >> i) % 2) * 2**(31 - i)
        return res

class Solution2:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res
