"""
https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
"""
from typing import List

class SolutionDP:
    """
    An extension of 416.canPartition.
    This question is equiv to paritioning a set into 2 subsets 
    such that the diff is minimum. We do this by determining the max
    sum < mean. 
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
    # we know that one of the sums has to be less than target
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1) # Index = True means you can attain sum = index  
        dp[0] = True

        for s in stones:
            for j in range(target, s - 1, -1):
                # print(target, j, s)
                dp[j] = dp[j] | dp[j - s]
        
        for i in range(target, -1, -1):
            # find the largest sum i <=> finding the min of the groups sums 
            if dp[i]:
                return abs((total - i) - i) 

class SolutionRecursive:
    """
    This may time out.
    Suppose you have two groups A & B. Their sums are sumA and sumB. We
    want to minimise abs(sumB - sumA).
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)

        def findMin(arr, counter, sumA):
            if counter == 0:
                # sumB = (totalSum - sumA)
                return abs((totalSum - sumA) - sumA) 

            # 2 options: either add stones[counter - 1] into the sumA          
            return min(findMin(arr, counter - 1, sumA + stones[counter - 1]),
                        findMin(arr, counter - 1, sumA))

        return findMin(stones, len(stones), 0)