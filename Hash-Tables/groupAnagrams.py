class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for n in strs:
            key = "".join(sorted(n))
            if key in hashmap:
                hashmap[key] = hashmap[key].append(n) 
            else:
                hashmap[key] = [n]
        
        return hashmap.values()