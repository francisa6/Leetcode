from typing import List


class SolutionSlow:
    def getRowPrev(self, rowIndex: int, colIndex: int) -> int:
        if rowIndex == colIndex or colIndex == 0:
            return 1
        else:
            return self.getRowPrev(rowIndex - 1, colIndex - 1) + self.getRowPrev(
                rowIndex - 1, colIndex
            )

    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (1 + rowIndex)
        numToCompute = rowIndex - rowIndex // 2
        for j in range(1, rowIndex):
            if j <= numToCompute:
                res[j] = self getRowPrev(rowIndex, j)
            else:
                res[j] = res[rowIndex - j]

        return res


class SolutionFast:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in [0, 1]:
            return [1] * (1 + rowIndex)

        else:
            prevRow = self.getRow(rowIndex - 1)
            for j in range(len(prevRow) - 1, 0, -1):
                prevRow[j] += prevRow[j - 1]
            return prevRow + [1]


rowIndex = 25
print("Solution is: ", SolutionFast().getRow(rowIndex))
