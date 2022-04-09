"""
O(nlogn) time
O(1) space as sort is in-place
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        for h in range(len(citations), 0, -1):

            if citations[h - 1] >= h:
                return h

        return 0
