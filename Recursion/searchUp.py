from typing import List
"""
Think of how to solve using binary search.
"""

class SolutionRecursive:
    """
    Uses the diagonal of the matrix to determine which submatrix to search.
    O(n*m/2) time complexity. Uses a lot of space because of the sub_matrix 
    redefining but we can stop redefining it to use O(1) space. 
    """    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def dfs(matrix, top, bottom):
            sub_matrix0 = matrix[top[0]:bottom[0]+1]
            sub_matrix = [mat_i[top[1]:bottom[1]+1] for mat_i in sub_matrix0]
            
            n, m = len(sub_matrix), len(sub_matrix[0])

            # base case includes the case when target is smaller than all numbers in the matrix
            if (sub_matrix[0][0] >= target) or sub_matrix[n-1][m-1] < target:
                if sub_matrix[0][0] == target:
                    return True
                return False
            
            diag = 0
            while diag < min([n, m]) and sub_matrix[diag][diag] < target:
                diag+=1
            
            if diag < min([n, m]) and sub_matrix[diag][diag] == target:
                return True

            if diag < min([n,m]):
                top = (0, diag)
                bottom = (diag-1, m-1)
                top1 = (diag, 0)
                bottom1 = (n-1, diag-1)
            elif m > n:
                top = (0, diag)
                bottom = (diag-1, m-1)
                top1 = (diag-1, diag-1)
                bottom1 = top1                
            elif n > m:
                top = (diag, 0)
                bottom = (n-1, diag-1)
                top1 = (diag-1, diag-1)
                bottom1 = top1                

            return dfs(sub_matrix, top, bottom) or dfs(sub_matrix, top1, bottom1)

        n, m = len(matrix), len(matrix[0])
        top, bottom = (0,0), (n-1,m-1)
        return dfs(matrix, top, bottom)


class RecursiveSolution2:
    """
    Uses binary search to determine which submatrix to discard. 
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                
        def dc(left,right,top,bottom):
            
            if left > right or top > bottom:
                # This is true when we have 1 value but that value isn't the target value
                return False
            
            rowmid = (top+bottom)//2
            colmid = (left+right)//2
            
            if matrix[rowmid][colmid] == target:
                return True
            
            elif target > matrix[rowmid][colmid]:
                return dc(colmid +1, right,top,rowmid) or dc(left,right,rowmid+1,bottom)
                
            elif target < matrix[rowmid][colmid]:
                return dc(left,right,top,rowmid-1) or dc(left,colmid-1,rowmid,bottom)
                        
        return dc(0,len(matrix[0])-1,0,len(matrix)-1)

class SolutionNeat:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        n, m = len(matrix), len(matrix[0])
        r = n-1
        c = 0

        while r >= 0 and c < m:
            if matrix[r][c] > target:
                r -=1
            elif matrix[r][c] < target:
                c +=1
            else:
                return True
        
        return False

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
matrix = [[4,7,11,12,16,21,23,26],[5,12,17,17,18,23,26,31],[8,15,21,25,26,29,33,34],[13,20,26,26,29,34,39,40],[18,21,31,36,41,42,42,44],[19,23,31,39,46,49,50,53],[23,25,33,40,50,51,55,60],[27,28,33,44,51,56,61,65],[32,35,39,45,54,56,65,68],[33,38,40,49,56,57,66,71]]
target = 5
print(SolutionNeat().searchMatrix(matrix, target))