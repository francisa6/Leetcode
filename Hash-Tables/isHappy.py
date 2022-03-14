# Time complexity?? and space complexity O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        storenums = {n}

        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n in storenums:
                return False
            storenums.add(n)

        return True
            

# Can also solve using Floyd cycle finding algo
