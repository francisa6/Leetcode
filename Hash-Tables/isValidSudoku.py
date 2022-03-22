import collections 

class Solution:
    def isValidSudoku1(self, board):
        return 1 == max(list(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i/3, j/3, c))
        ).values()) + [1])
    # The + [1] is only for the empty board, where max would get an empty list and complain. It's not necessary to get it accepted here, as the empty board isn't among the test cases, but it's good to have.


# Creates a list! sum((['a'], ['b']), []) = ['a', 'b'] don't know why though?
    def isValidSudoku2(self, board):
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))


# seen.add(x) will always evaluate just depends on whether 'x in seen' is true or false
    def isValidSudoku3(self, board):
        seen = set()
        return not any(x in seen or seen.add(x)
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'
                    for x in ((c, i), (j, c), (i/3, j/3, c)))


    class Solution:
        def checkDups(self, listCheck) -> bool:
            for l in listCheck.values():
                if len(set(l)) != len(l):
                    return False
            return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        square = {}

        for i in range(9):
            for j in range(9):
                # Row
                if board[i][j] != ".":
                    row[i] = row.get(i, []) + [board[i][j]]

                # Column
                    column[j] = column.get(j, []) + [board[i][j]]

                # Square
                    key = f'{i // 3}' + f'{j // 3}'
                    square[key] = square.get(key, []) + [board[i][j]]

        # Check if dups
        return self.checkDups(square) and self.checkDups(column) and self.checkDups(row)

