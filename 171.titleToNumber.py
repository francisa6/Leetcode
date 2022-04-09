class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        res = 0
        
        for e, c in enumerate(reversed(columnTitle)):
            res += 26**e * (ord(c) - ord('A') + 1)
        
        return res