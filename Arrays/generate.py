from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]

        # Initialise first 2 rows depending on numRows  
        if numRows >= 1:
            res[0] = [1]
        
        if numRows > 1:
            res[1] = [1,1]

        # take the two values and add them up and put 1 on either side
        # Repeat until numRows is reached
        j = 2
        while j < numRows:
            prev_res = res[j-1]
            res[j] = [1] + [prev_res[i-1] + prev_res[i] for i in range(1, len(prev_res))] + [1]
            j +=1

        return res


numRows = 5
print(Solution().generate(numRows))

