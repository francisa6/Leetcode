"""
O(n) time and O(1) space
"""
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for w in words:
            if w == w[::-1]:
                return w
        return ""


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalindrome(w):
            l = 0
            r = len(w) - 1

            while l <= r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True

        for w in words:
            res = checkPalindrome(w)
            if res:
                break
        return w if res else ""


class SolutionGenerator:
    """
    Only gives you the first 1 when using next
    """

    def firstPalindrome(self, words: List[str]) -> str:

        return next((w for w in words if w == w[::-1]), "")


words = ["abc", "car", "ada", "racecar", "cool"]

sol = SolutionGenerator().firstPalindrome(words)

print(sol)

