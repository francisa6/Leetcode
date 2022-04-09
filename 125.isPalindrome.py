"""
O(n) time
O(1) space unless using .lower() which is O(n) as it is not inplace
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        l = 0
        r = len(s) - 1

        while l <= r:

            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s.lower()[l] == s.lower()[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
