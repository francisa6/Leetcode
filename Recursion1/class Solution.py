# This is a bottom up approach - time complex is only n (as we don't count the cheap memomization)
class Solution:
    def climbStairsMemoization(self, n: int) -> int:
        # This function tells you the number of possibilities at n steps
        cache = {}

        def climbStairSub(n: int) -> int:
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            elif n == 2:
                return 2

            # Add the possibilities after taking 1 step and 2 steps and look at the number of possibilities left
            res = climbStairSub(n - 1) + climbStairSub(n - 2)
            cache[n] = res
            return cache[n]

        return climbStairSub(n)

    def climbStairs(self, n: int) -> int:
        cache = [None] * n
        cache[0], cache[1] = 1, 2

        def climbStairSub(n: int) -> int:
            res = cache[n - 2] + cache[n - 3]
            cache[n - 1] = res
            return res

        for i in range(3, n + 1):
            _ = climbStairSub(i)

        return cache[n - 1]


# def climbStairs(self, n):
#     a, b = 1, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a


n = 5

print(f"Solution n = {n} has ", Solution().climbStairs(n), " possibilities.")
