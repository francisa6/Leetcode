##### Daily Temperature -- Really Nice #####

from os import terminal_size
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lenTemp = len(temperatures)
        res = [0] * lenTemp

        for i, temp in enumerate(temperatures[:-1]):
            j = i + 1
            while j < lenTemp:
                if temp < temperatures[j]:
                    res[i] = j - i
                    break
                j += 1

        return res

    def dailyTemperaturesStackForward(self, temperatures: List[int]) -> List[int]:
        # Use stack to keep track of indices that need to be updated later.
        # Note we only look at stack[-1] because stack contains elements in decreasing order
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j

            stack.append(i)
        return res

    def dailyTemperaturesStackBackward(self, temperatures: List[int]) -> List[int]:
        # Use stack to keep track of indices that need to be updated later.
        # Note we only look at stack[-1] because stack contains elements in decreasing order
        stack = []
        # stores elements in the future and drop the future most obs if it is not bigger than what we curr have
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and (temperatures[stack[-1]] <= temperatures[i]):
                stack.pop()

            res[i] = stack[-1] - i if stack else 0

            stack.append(i)

        return res


# temperatures = [30, 60, 90]
# temperatures = [30, 40, 50, 60]
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print("Solution is: ", Solution().dailyTemperaturesStackBackward(temperatures))
