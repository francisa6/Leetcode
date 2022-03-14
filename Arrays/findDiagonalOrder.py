from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j = 0, 0
        n, m = len(mat), len(mat[0])

        res = []
        i_dir = -1
        while len(res) < m*n:
            # print(res, i, j)
            res.append(mat[i][j])

            if (0<=(i+i_dir) < n and 0 <=(j-i_dir) < m):
                i += i_dir
                j -= i_dir
            elif i_dir < 0 and (j + 1) < m:
                j+=1
                i_dir *= -1
            elif i_dir < 0 and (i+1 < n):
                i+=1
                i_dir *= -1
            elif i_dir > 0 and (i + 1) < n:
                i+=1
                i_dir *= -1
            elif i_dir > 0 and (j+1) < m:
                j+=1
                i_dir *= -1
                
        return res

mat =  [[2],[3]] #[[1,2],[3,4]] #[[1,2,3],[4,5,6],[7,8,9]]


print(Solution().findDiagonalOrder(mat))