from typing import List

class SolutionDP:
    """
    Resolves the issue with duplicates entries.
    Use DP to reduce to polynomial time with more space.
    O(n sum(nums)) time complex 
    O(sum(nums)) space complex 
    """
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False 

        target = total // 2
        res = [False] * (target + 1) # what index is attainable
        res[0] = True

        for n in nums:
            # if you have [3, 1] then the 3 would never actually contribute     
            # need to go backwards not forwards otherwise it's wrong e.g. if looping forward [1] would mark all list entries True
            for j in range(target, n - 1, -1): 
                res[j] = res[j] | res[j - n] # check if from res[j-n] that res[j] is attainable given th number n
        
        return res[target]

class Solution:
    """
    Naive method which takes O(2**n) time and wastes a lot of space
    """
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2 
        res = set([0])
        for n in nums:
            for r in frozenset(res): # freeze so the set doesn't change size 
                n_new = r + n
                if n_new == target:
                    return True
                res.add(n_new)
        return False

class SolutionRecursion:
    """
    Recursion which takes O(n2**n) time but saves space
    """
    def canPartition(self, nums: List[int]) -> bool:
        self.res = False

        def recurse(index, val):
            if val == sum(nums) / 2:
                self.res = True
                return  
            elif index == len(nums):
                return 
            
            recurse(index + 1, val)
            recurse(index + 1, val + nums[index])

        recurse(0, 0)
        return self.res

