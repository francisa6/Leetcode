class Solution:
    def searchUp(self, matrix, target, fixed_col, end, start):
        for i in range(end, start-1, -1 ):
            if matrix[i][fixed_col] == target:
                return True
        return False
    def searchLeft(self, matrix, target, fixed_row, end, start):
        for i in range(end, start-1, -1):
            if matrix[fixed_row][i] == target:
                return True
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row and column
            m,n = matrix.shape                 
            i, j = 0, 0
            while matrix[0][j] > target:
                j+=1
            
            while matrix[i][0] > target:
                i+=1
            
            return self.searchUp(matrix, target, j-1, i-1, 0) or self.searchLeft(matrix, target, i-1, j-1, 0)

matrix = 
print(Solution().searchMatrix(matrix, target))