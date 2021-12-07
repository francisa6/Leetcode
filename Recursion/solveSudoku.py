# from Typing import List 

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numRowsBoard = int(len(board)**0.5)
        def existingValuesDict(pos):
            i,j = emptySpots[pos]
            col = set([board[ii][j] for ii in range(numRowsBoard**2) if board[ii][j] != "."])
            # print(col, len(col))
            row = set([board[i][jj] for jj in range(numRowsBoard**2) if board[i][jj] != "."])
            # print(row, len(row))
            row_sub, col_sub = int((i // numRowsBoard)*numRowsBoard), int((j // numRowsBoard)*numRowsBoard)
            square = set([board[ii][jj] for ii in range(row_sub, row_sub+numRowsBoard) for jj in range(col_sub, col_sub+numRowsBoard) if board[ii][jj] != "."])
            return {'col': col, 'row': row, 'square': square}

        def checkIfValueIsValid(pos, existingVals, v):
            col = existingVals['col']
            row = existingVals['row']
            square = existingVals['square']
            # print(square, len(square), type(v) )
            # if len(col) == len(col.add(v)) or len(row) == len(row.add(v)) or len(square) == len(square.add(v)):
            if v in col or v in row or v in square:
                return False
                
            i, j = emptySpots[pos]
            board[i][j] = v 
            return True

        def removeRecentlyAddedValue(pos):
            i,j = emptySpots[pos]
            board[i][j] = "."

        emptySpots = [(i, j) for i in range(numRowsBoard**2) for j in range(numRowsBoard**2) if board[i][j] == "."]
        totalEmptySpots = len(emptySpots)
        foundSol = False

        def fixPosition_solveSudoku(pos):
            """
            Global variables: board, emptySpots, totalEmptySpots
            Want to break when we find a solution unlike totalNQueens.py
            Need nonlocal foundSol because we are changing the value of foundSol inside this function.
            """
            nonlocal foundSol
            # print(board, 'pos: ', pos)
            # Similar to Memoization
            existingVals = existingValuesDict(pos)
            # print('existingVals: ', existingVals) 

            for v in range(1, numRowsBoard**2 + 1):
                # print('v: ', v)
                if not foundSol and checkIfValueIsValid(pos, existingVals, str(v)):
                    next_pos = pos + 1
                    if next_pos >= totalEmptySpots:
                        # print( 'next_pos: ', next_pos, "board temp: ", board)
                        foundSol = True
                        return 
                    fixPosition_solveSudoku(next_pos)
                    # print('v: ', v, 'pos: ', pos, "board: ", board)
                    if not foundSol:
                        removeRecentlyAddedValue(pos) 

        fixPosition_solveSudoku(0)
        # print("board temp2: ", board)



class Solution2:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.numRowsBoard = int(len(self.board)**0.5)
        self.emptySpots = [(i, j) for i in range(self.numRowsBoard**2) for j in range(self.numRowsBoard**2) if self.board[i][j] == "."]
        self.foundSol = False
        self.fixPosition_solveSudoku(0)
        print("self.board temp2: ", self.board)

    def existingValuesDict(self, pos):
        i,j = self.emptySpots[pos]
        col = set([self.board[ii][j] for ii in range(self.numRowsBoard**2) if self.board[ii][j] != "."])
        row = set([self.board[i][jj] for jj in range(self.numRowsBoard**2) if self.board[i][jj] != "."])
        row_sub, col_sub = int((i // self.numRowsBoard)*self.numRowsBoard), int((j // self.numRowsBoard)*self.numRowsBoard)
        square = set([self.board[ii][jj] for ii in range(row_sub, row_sub+self.numRowsBoard) for jj in range(col_sub, col_sub+self.numRowsBoard) if self.board[ii][jj] != "."])
        return {'col': col, 'row': row, 'square': square}

    def checkIfValueIsValid(self, pos, existingVals, v):
        col = existingVals['col']
        row = existingVals['row']
        square = existingVals['square']
        # print(square, len(square), type(v) )
        # if len(col) == len(col.add(v)) or len(row) == len(row.add(v)) or len(square) == len(square.add(v)):
        if v in col or v in row or v in square:
            return False
            
        i, j = self.emptySpots[pos]
        self.board[i][j] = v 
        return True

    def removeRecentlyAddedValue(self, pos):
        i,j = self.emptySpots[pos]
        self.board[i][j] = "."

    def fixPosition_solveSudoku(self, pos):
        """
        Global variables: self.board, emptySpots, totalEmptySpots
        Want to break when we find a solution unlike totalNQueens.py
        """
        print(self.board, 'pos: ', pos)
        # Similar to Memoization
        existingVals = self.existingValuesDict(pos)
        print('existingVals: ', existingVals)

        for v in range(1, self.numRowsBoard**2 +1):
            print('v: ', v)
            if not self.foundSol and self.checkIfValueIsValid(pos, existingVals, str(v)):
                next_pos = pos + 1
                if next_pos >= len(self.emptySpots):
                    print( 'next_pos: ', next_pos, "self.board temp: ", self.board)
                    self.foundSol = True
                    return 
                self.fixPosition_solveSudoku(next_pos)
                print('v: ', v, 'pos: ', pos, "self.board: ", self.board)
                if not self.foundSol:
                    self.removeRecentlyAddedValue(pos) 




# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# board = [["1","2", "3", "."], ["3","4", "1", "."], ["4","3", "2", "1"], ["2","1", "4", "3"]]
board = [["1",".", ".", "."], ["3",".", ".", "."], ["4","3", ".", "."], ["2","1", "4", "3"]]
Solution2().solveSudoku(board)
print('Final result: ', board)
