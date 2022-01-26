
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # make a the shorter string
        if len(b) < len(a):
            a, b = b, a
        a = "0"*(len(b) - len(a)) + a

        # define carry and res
        carry = 0 
        res = ""

        # while a is valid add and normalise 
        i = len(a) - 1
        while i >= 0:
            sum_ab = int(a[i]) + int(b[i]) + carry
            remainder = sum_ab % 2
            carry = sum_ab//2
            res = str(remainder) + res
            i-=1

        # make adjustment according to b and carry
        if carry > 0:
            res = "1" + res
        
        return res

a = "1010" 
b = "1011"
print(Solution().addBinary(a, b))