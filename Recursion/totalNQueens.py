class Solution:

    def totalNQueens(self, n: int) -> int:
        board = [[0 for _ in range(n)] for _ in range(n)]

        def is_not_under_attack(row, column):
            # Check diag, row, column
            for d in range(1, n):
                if (column + d < n and board[row][column + d] > 0) or \
                     (column - d >= 0 and board[row][column - d] > 0) or \
                     (row + d < n and board[row + d][column] > 0) or \
                     (row - d >= 0 and board[row - d][column] > 0):
                    return False
                if (row + d < n and column + d < n and board[row + d][column + d] > 0) or \
                    (row - d >= 0 and column - d >= 0 and board[row - d][column - d] > 0) or \
                    (row - d >= 0 and column + d < n and board[row - d][column + d] > 0) or \
                    (row + d < n and column - d >= 0 and board[row + d][column - d] > 0):
                    return False 
            # place piece on the board
            board[row][column] = 1 
            return True
        
        def remove_queen(row, column):
            board[row][column] = 0  

        def backtrackQueen(row = 0, count = 0):
            # iterate over each possible column on the board for a fixed row  
            for column in range(n):
                # check if the (row, column) is under attack
                if is_not_under_attack(row, column):
                    # put the piece in the position
                    if row + 1 == n:
                        # end of the board
                        print(board)
                        count+=1
                    else:
                        count = backtrackQueen(row +1, count)
                    
                    # remove the piece just put because we want to test for next (row, column) combination
                    remove_queen(row, column)
            return count

        return backtrackQueen(0, 0)

n = 3
print(Solution().totalNQueens(n))