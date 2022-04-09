"""
O(n) space
O(n) time
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}

        for c in s:
            letters[c] = letters.get(c, 0) + 1

        longestLength = 0
        oddCounter = 0
        for v in letters.values():
            if v % 2 == 1:
                oddCounter += 1

            longestLength += v

        return longestLength - oddCounter + (oddCounter > 0)


class SolutionSet:
    def longestPalindrome(self, s: str) -> int:

        oddSet = set()

        for c in s:
            if c in oddSet:
                oddSet.remove(c)
            else:
                oddSet.add(c)

        return len(s) - len(oddSet) + (len(oddSet) > 0)
