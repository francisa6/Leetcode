"""
O(n) time 
O(1) space
"""

from typing import List
from types import GeneratorType


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        thres = len(arr) / 4

        def checkCount(thres, count):
            return count > thres

        count = 0
        prev = -1
        for i in arr:
            if prev != i:
                if checkCount(thres, count):
                    return prev
                count = 0
                prev = i
            count += 1

        return i


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        res = {}
        for a in arr:
            res[a] = res.get(a, 0) + 1

        maxVal = max(res.values())

        return next(k for k, v in res.items() if v == maxVal)


print(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))

