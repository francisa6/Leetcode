# [0] is another example of using dummy variables to prevent an error namely 
# "closeStackTrue.pop" similar to prenode 

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{": "}", "(": ")", "[": "]"}
        closeStackTrue = [0]
        
        for i in s:

            if i in brackets:
                closeStackTrue.append(brackets[i])

            elif closeStackTrue.pop() != i:
                return False

        return closeStackTrue == [0]


# s = "{[]}"
# s = "(]"
s = "()[]{}"
# s = "()"

print(f"Is {s} valid:", Solution().isValid(s))
