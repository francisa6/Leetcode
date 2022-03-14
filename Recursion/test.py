class hi:
    # def change_board(self, x):
    #     self.board[0][1] = 1
    def f(self, board):

        def it(pos):
            if pos == 2:
                return True
            board[pos] = 1
            it(pos+1)
        it(0)
        


board = [0 for _ in range(5)]
org_board = board
print('org_board: ', org_board )
hi().f(board)
print('board: ', board )