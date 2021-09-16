from typing import List

# The recursive solution is very slow, because its runtime is exponential
# https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/discuss/97334/Java-(15-ms)-C++-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanation


class SolutionRecursive:
    def __init__(self):
        self.res = 0
        # self.operation = {"+": lambda x, y: x+y, "-": lambda x, y: x-y}

    def findTargetSumSub(self, nums: List[int], acc: int, ind: int, target: int):
        # acc = self.operation[s](acc, nums[ind])
        if ind == len(nums):
            if acc == target:
                self.res += 1
            return

        self.findTargetSumSub(nums, acc + nums[ind], ind + 1, target)
        self.findTargetSumSub(nums, acc - nums[ind], ind + 1, target)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.findTargetSumSub(nums, 0, 0, target)
        return self.res


from collections import deque


class SolutionQueue:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # nums is the queue
        acc = deque([0])

        while nums:
            q = nums.pop(0)
            for _ in range(len(acc)):
                a = acc.popleft()
                acc.append(a + q)
                acc.append(a - q)

        res_list = [1 for a in acc if a == target]
        return sum(res_list)


# nums = [25, 29, 23, 21, 45, 36, 16, 35, 13, 39, 44, 15, 16, 14, 45, 23, 50, 43, 9, 15]
# target = 32
nums = [1, 1, 1, 1, 1]
target = 3


print("Solution: ", SolutionQueue().findTargetSumWays(nums, target))
