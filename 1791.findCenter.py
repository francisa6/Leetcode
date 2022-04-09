"""
O(1) time and space
"""
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        v = {}

        for e1, e2 in edges:
            v[e1] = v.get(e1, 0) + 1
            v[e2] = v.get(e2, 0) + 1

        return next((e for e, val in v.items() if val == max(v.values())))


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        e1 = edges[0][0]
        e2 = edges[0][1]

        if e1 in edges[1]:
            return e1
        return e2
