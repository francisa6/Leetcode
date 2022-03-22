from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:

        original = [k ** 2 for k in range(1, int(n ** (0.5) + 1))]
        level = 0
        queue = deque()
        queue.append(0)

        while True:
            level += 1
            for _ in range(len(queue)):
                qcurr = queue.popleft()

                for e in original:

                    curr = qcurr + e

                    if curr == n:
                        return level
                    if curr < n:
                        queue.append(curr)


n = 13
print(f"n = {n}: ", Solution().numSquares(n))
