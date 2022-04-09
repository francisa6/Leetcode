class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenWord = 0
        
        for w in s[::-1]:
            if w == " " and lenWord > 0:
                return lenWord
            elif w != " ":
                lenWord += 1
        return lenWord