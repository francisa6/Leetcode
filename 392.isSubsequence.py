"""
O(n) time 
O(1) space
"""

class SolutionFast:
    # https://stackoverflow.com/questions/24017363/how-to-test-if-one-string-is-a-subsequence-of-another/24017747#24017747
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t) # iter yields items not previously yielded
        return all(c in t for c in s) # all gives you true if everything in the iterator is true
 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        i = 0
        for j in t:
            if j == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False