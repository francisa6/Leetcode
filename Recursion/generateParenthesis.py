
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generateParenthesisSub(s: str, num_left: int, num_right: int):
            if num_right == n:
                res.append(s)
                return 

            else:
                if num_left < n:
                    generateParenthesisSub(s + "(", num_left + 1, num_right)
                
                if num_right < n and num_left > num_right:
                    generateParenthesisSub(s + ")", num_left, num_right + 1)
        
        generateParenthesisSub("", 0, 0)            
        
        return res

n = 4
# print(Solution().generateParenthesis(n))


class SolutionIterative:
    def generateParenthesis(self, n: int) -> List[str]:
        s, num_left, num_right = "", 0, 0
        stack = [(s, num_left, num_right)]
        res = []
        while stack:
                # print(stack)
                s, num_left, num_right = stack.pop(0)
                if num_left < n:
                    stack.append((s + "(", num_left + 1, num_right))
                
                if num_right < n and num_left > num_right:
                    stack.append((s + ")", num_left, num_right + 1))

                if len(s) == 2*n:
                    res.append(s)
            
        return res
        

n = 1
# print(SolutionIterative().generateParenthesis(n))


###### Nice Solutions
def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))

def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)

def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)

def generateParenthesis(n):
    res = []
    if n == 0:
        return [""]
    else:
        for i in range(n):
            for k in generateParenthesis(i):
                for j in generateParenthesis(n-i-1):
                    res.append('(' + k + ')' + j)
    return res

n = 3
print(generateParenthesis(n))