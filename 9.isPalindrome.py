"""
O(n) time
O(1) space
"""


class SolutionBetter:
    """
    This handles negative values because -1 % 10 = 9 so we wouldn't be able to
    get the reverse back. 
    """

    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed = 0
        while x > 0:

            reversed = (original * 10) + (x % 10)
            x = x // 10

        return original == reversed


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        d = 0
        while (x // (10 ** d)) > 0:
            d += 1

        l = 10 ** (d - 1)
        r = 10

        while l >= r:

            if ((x // l) % 10) != ((x % r) // (r / 10)):
                return False

            l /= 10
            r *= 10

        return True
