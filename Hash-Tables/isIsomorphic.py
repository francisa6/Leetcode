class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}

        for s_i, t_i in zip(s, t):
    
            if s_i in hashmap.keys():
                if hashmap[s_i] != t_i:
                    return False
            hashmap[s_i] = t_i   

            if t_i in hashmap2.keys():
                if hashmap2[t_i] != s_i:
                    return False
            hashmap2[t_i] = s_i

        return True
            
    def isIsomorphicFaster(self, s:str , t:str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))

    def isIsomorphicNice(self, s, t): 
        # Use the position vector 
        return [s.find(i) for i in s] == [t.find(j) for j in t]
