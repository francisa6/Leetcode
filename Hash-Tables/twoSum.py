# O(N) time complexity and O(N) space complexity
# Will get O(N**2) time complexity if you use the 2 pointer method

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for e, n in enumerate(nums):
            altkey = target - n 

            if altkey in hashmap.keys():
                return [e, hashmap[altkey][altkey]]

            if n in hashmap.keys():
                if hashmap[n][altkey]:
                    return [e, hashmap[n][altkey]]
            else:
            # If latkey == n then it takes the last key, value pair
                hashmap[n] = {altkey: None, n: e}


    def twoSumLessMemory(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for e, n in enumerate(nums):
            altkey = target - n
            if altkey in hashmap:
                return [e, hashmap[altkey]]

            else:
                hashmap[n] = e