from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
        }
        stackVal = []

        for t in tokens:
            if t in operator:
                a = stackVal.pop()
                b = stackVal.pop()
                stackVal.append(operator[t](int(b), int(a)))
            else:
                stackVal.append(t)
        return stackVal[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["0", "3", "/"]
print("Solution: ", Solution().evalRPN(tokens))
