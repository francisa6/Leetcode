"""
O(n) time for reversing and also loop.
O(1) space because reversed is a generator.
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        sym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        past = "I"

        for c in reversed(s):

            val = sym[c]
            if sym[c] < sym[past]:
                val *= -1

            res += val
            past = c

        return res
