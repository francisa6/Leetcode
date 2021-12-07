from typing import List

"""
From [1,3] to get back to [1] we need to remember to 'return res_temp' 
otherwise the res_temp after the last added element is removed doesn't get remembered.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combine_sub(start, res_temp):
            if 0 < len(res_temp) < k or (len(res_temp) == 0 and (n+1) - start >= k):
                for i in range(start, n+1):
                    res_temp.append(i)
                    if len(res_temp) == k:
                        res.append(res_temp)
                    res_temp = combine_sub(i+1, res_temp)
                    # remove what the element of res_temp just added
                    res_temp = res_temp[:-1]
            return res_temp

        res = []
        start = 1
        combine_sub(start, [])
        return res

class SolutionFaster:
    """
    This is a neat trick because we don't assign anything to res_temp -- in the previous solution we had 
    to manually remove the most recently added element because the list is mutable! 
    Here we are also iterating over more values than required e.g. when n > k we are iterating over n when
    we know that the last value can't have anything else added to it to make the list have length k.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(start, res_temp):
            print(res_temp)
            if len(res_temp) == k:
                res.append(res_temp)
                return 
            
            for i in range(start, n+1):
                dfs(i+1, res_temp + [i])

        res = []
        dfs(1, [])
        return res

n = 8
k = 3
print(SolutionFaster().combine(n, k))