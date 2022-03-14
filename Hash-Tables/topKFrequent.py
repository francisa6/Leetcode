# A heaps takes n log n time complex

import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = collections.Counter(nums).most_common(k)

        return [tuple_val[0] for tuple_val in countdict]

# O(3N) memory and O(N) time
class SolutionExtended:
    def topKFrequent(self, nums: List[int], k : int) -> List[int]:
        map1 = {}
        running_max_val = 0
        for n in nums:
            val = 1
            if n in map1.keys():
                val = val + map1[n] 
            map1[n] = val

            running_max_val = max(val, running_max_val)

        key_store = [[] for _ in range(running_max_val)]
        for key, v in map1.items():
            key_store[v-1].append(key)
        
        return_keys = []
        i = running_max_val-1
        while len(return_keys) !=k:
            if key_store[i] != []:
                return_keys = return_keys + key_store[i]
            i -=1
        return return_keys
        


        


            