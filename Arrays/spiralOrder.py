

# Right, down, left, up until you can't do either

# can't go right anymore j + 1 > m: +=top
# can't go down anymore: -= right_col
# can't go left anymore: -=bottom
# can't go up anymore: += left_col

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        res = [matrix[0][0]] if m != 0 else [] 
        left_bound = -1
        top_bound = -1
        right_bound = m
        bottom_bound = n

        i, j = 0, 0
        while len(res) < n * m:

            while len(res) < n * m and j + 1 < right_bound:
                j+=1
                res.append(matrix[i][j])
            top_bound +=1
            
            while len(res) < n * m and i + 1 < bottom_bound:
                i+=1
                res.append(matrix[i][j])
            right_bound -=1

            while len(res) < n * m and j - 1 > left_bound:
                j-=1
                res.append(matrix[i][j])
            bottom_bound -=1

            while len(res) < n * m and i - 1 > top_bound:
                i-=1
                res.append(matrix[i][j])
            left_bound +=1

        return res

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(mat))