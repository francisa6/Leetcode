class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Construct Stack of positions 
        stack = [k]
        for l in range(1, n-1):
            s = stack[l-1]
            if s % 2 == 0:
                stack.append(s/2)
            else:
                stack.append(round(s/2 + 0.5))

        def kthGrammarSub(stack, currDigit):

            if not stack:
                return currDigit

            if currDigit == 1:
                possibleComb = [1, 0]    
            else:
                possibleComb = [0, 1]    
            
            s = stack.pop()
            if s % 2 == 0:
                return kthGrammarSub(stack, possibleComb[1])
            else:
                return kthGrammarSub(stack, possibleComb[0])

        return kthGrammarSub(stack, 0)


# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/discuss/427711/Python-recursive-solution-No-binary
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 and K==1: return 0
        if K%2:
            return self.kthGrammar(N-1, K//2+1)
        if self.kthGrammar(N-1, K//2)==0: return 1
        if self.kthGrammar(N-1, K//2)==1: return 0

n = 2
k = 2
print(Solution().kthGrammar(n, k))