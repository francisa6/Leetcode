# O(2N) approx O(N) time complexity and O(1) space

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for s_i in s:
            hashmap[s_i] += 1
        
        for e, s_i in enumerate(s):
            if hashmap[s_i] == 1:
                return e
        return -1