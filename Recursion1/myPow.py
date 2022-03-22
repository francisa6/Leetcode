from typing import AsyncContextManager


class Solution:
    # Space O(1) complexity (actually should be O(2) for tail recursion and 1/go(1-n)) and time complexity is N time.
    # This should still be considered tail recursion because the last operation of the 
    # recursion is a recursive call
    def myPowTailRecursion(self, x: float, n: int) -> float:
        def go(acc, n):
            if n==0:
                return acc
            return go(acc*x, n-1)

        if n < 0:
            return 1/go(1, -n)
        return go(1, n)

# Uses a bit of tail recursion but not all
    def myPowfaster(self, x:float, n:int) -> float:
       
        def myPowSub(acc, x, n):
            if n == 0:
                return acc

            if n < 0:
                return myPowSub(acc, 1/x, -n)
            
            if n % 2 ==0:
                res = myPowSub(1, x, n // 2)
                return acc * res * res

            return myPowSub(acc*x, x, n-1)

        return myPowSub(1, x, n)


# Space complexity and time complexity is log(N) time because of the n//2. 
# Note all space used is recursion related and there is none that can be memorized. 
# This doesn't use tail recursion
    def myPow(self, x:float, n:int)->float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        
        myHalfPow = self.myPow(x, n//2)

        if n % 2 == 0:
            return myHalfPow * myHalfPow
        
        return myHalfPow * myHalfPow * x



x =26
n =-25
# x = 2
# n= 2
print(Solution().myPowfaster(x, n), 'same as ', x**n)
print(Solution().myPow(x, n), 'same as ', x**n)