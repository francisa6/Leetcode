from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        break_true = False
        while i < len(strs[0]) and not break_true:
            j = 0            
            letter = strs[j][i]
            while j < len(strs)-1:
                j +=1
                if not (i < len(strs[j]) and strs[j][i] == letter):
                    break_true = True
                    break
            if break_true:
                break
            res += letter
            i+=1
        
        return res  

# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["ab", "a"]
strs = ["dog"]

# print(Solution().longestCommonPrefix(strs))


class SolutionNeat:
    """
    Only need to check the last one after sorting.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res

        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                res += x
            else:
                break
        return res

print(Solution().longestCommonPrefix(strs))

