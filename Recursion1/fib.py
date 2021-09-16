class Solution:
    def fib(self, n: int) -> int:
        # Define dictionary
        cache = {}

        def fibSub(n: int) -> int:
            # If it has already been calculated
            if n in cache:
                return cache[n]

            # If it has not been calculated
            # Base case
            if n == 0:
                res = 0
            elif n == 1:
                res = 1
            else:
                res = fibSub(n - 1) + fibSub(n - 2)
            # print("cache", cache)
            cache[n] = res
            return cache[n]

        return fibSub(n)


print("Solution: ", Solution().fib(3))
