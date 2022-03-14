# from typing import int

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, len(n)

        while l < r:
            mid = (l + r) // 2

            if not isBadVersion(mid + 1):
                l = mid + 1
            else:
                r = mid

        # when l == r
        return l + 1
