"""
O(n) time and O(1) space.

"""


class Solution:
    def reverse(self, x: int) -> int:

        sign = 1
        if x < 0:
            sign = -1
        x *= sign

        rev = 0
        org = x
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10

        rev = sign * rev

        return rev if -(2 ** 31) - 1 < rev < 2 ** 31 else 0


class SolutionStr:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        x *= sign

        rev = sign * int(str(x)[::-1])
      
        return rev if -(2 ** 31) - 1 < rev < 2 ** 31 else 0