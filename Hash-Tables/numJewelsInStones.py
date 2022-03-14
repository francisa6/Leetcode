# O(jewels len + stones len) tc and space is O(jewels len)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelStoneType = {j: 0 for j in jewels}

        for j in stones:
            if j in jewelStoneType:
                jewelStoneType[j] +=1

        return sum(jewelStoneType.values())
        
    def numJewelsInStonesFast(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
    
    def numJewelsInStonesFast2(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))