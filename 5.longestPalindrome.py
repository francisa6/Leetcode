"""
https://en.wikipedia.org/wiki/Longest_palindromic_substring
Manacher's algorithm is a much faster version! 
O(n) time and O(n) space
"""


class SolutionNaive:
    def longestPalindrome(self, s: str) -> str:

        # do this to make the s have odd length
        sn = "|" + "|".join(s) + "|"  # has length (2 * n + 1)
        radius_store = [0] * len(sn)
        c = 0

        while c < len(sn):

            radius = 0
            while (
                (c - radius >= 0)
                and (c + radius < len(sn))
                and sn[c - radius] == sn[c + radius]
            ):
                radius += 1

            # inclusive of end points
            radius_store[c] = radius - 1
            c += 1

        max_radius = max(radius_store)
        max_center = radius_store.index(max_radius)  # gets first occurance

        ss = sn[max_center - max_radius : max_center + max_radius + 1]

        return ss.replace("|", "")


s = "cbbd"
print(SolutionNaive().longestPalindrome(s))


# TBC
# class SolutionManacher:
#     def longestPalindrome(self, s: str) -> str:

#         # do this to make the s have odd length
#         sn = "|" + "|".join(s) + "|"  # has length (2 * n + 1)
#         radius_store = [0] * len(sn)

#         c = 0
#         radius = 0

#         while c < len(sn):

#             while (
#                 (c - (radius + 1) >= 0)
#                 and (c + (radius + 1) < len(sn))
#                 and sn[c - (radius + 1)] == sn[c + (radius + 1)]
#             ):
#                 radius += 1

#             # inclusive of end points
#             radius_store[c] = radius

#             old_center = c
#             old_radius = radius
#             c += 1

#             radius = 0
#             while c <= old_center + old_radius:
#                 mirriored_center = old_center - (c - old_center)

#                 max_mirrored_radius = old_center + old_radius - c

#                 if radius_store[mirriored_center] < max_mirrored_radius:
#                     radius


# s = "cbbd"
# print(SolutionManacher().longestPalindrome(s))


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         sr = reversed(s)

#         def longestPal(i, j):
#             if s[i:j] in sr:
#                 return s[i:j]

#             l = longestPal(i, j - 1)

#             r = longestPal(i + 1, j)

#             return l if len(l) > len(r) else r

#         return longestPal(0, len(s) - 1)

