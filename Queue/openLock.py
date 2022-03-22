from collections import deque
from typing import Sequence

# Deque is preferred over list in the cases where
# we need quicker append and pop operations from both
# the ends of container, as deque provides an O(1) time
# complexity for append and pop operations as
# compared to list which provides O(n) time complexity.

# Lists in python are arrays (stored in continguous areas of memory). Sets
# are implemented in a hash table. So searching for whether something exists
# is much faster when using a set.

# Note: I got speed issues when using a list and encountered recurisve depth
# issues when using a recursion.


class Solution:
    # Queue is a set of completely different elements (and are not elements of seencombinations)
    def openLock(self, deadends: List[str], target: str) -> int:
        seencombinations = set(deadends)
        level = 0
        queue = deque()
        queue.append("0000")

        # We need this because checks are not applied to the starting combination

        while queue:

            for _ in range(len(queue)):
                q = queue.popleft()

                if q == target:
                    return level

                if q in seencombinations:
                    continue
                seencombinations.add(q)

                for i in range(4):
                    digit = int(q[i])
                    for operation in [-1, 1]:
                        queue.append(q[:i] + str((digit + operation) % 10) + q[i + 1 :])

            level += 1

        return -1


# deadends = ["0010"]
# target = "1111"
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
# deadends = ["8888"]
# target = "0009"
# deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
# target = "8888"
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(
    f"Solution to deadends {deadends} and target {target} is",
    Solution().openLock(deadends, target),
)


# Bad as reaches recursion depth
# class Solution:
#     def __init__(self):
#         self.possiblelevels = -1
#         self.seencombinations = []

#     def percombination(self, currlock, deadends, target, level):
#         print("currlock", currlock)
#         if currlock == target:
#             self.possiblelevels = min(self.possiblelevels, level)

#         if (
#             (currlock in deadends)
#             or (currlock == target)
#             or (currlock == "0000" and level != 0)
#             or (currlock in self.seencombinations)
#         ):
#             return

#         if currlock not in self.seencombinations:
#             self.seencombinations.append(currlock)
#             print("self.seencombinations", self.seencombinations)

#         q_list_plus, q_list_minus = list(currlock), list(currlock)
#         for i in range(4):
#             q_list_plus[i] = str((int(currlock[i]) + 1) % 10)
#             q_list0 = "".join(q_list_plus)
#             self.percombination(q_list0, deadends, target, level + 1)

#             q_list_minus[i] = str((int(currlock[i]) - 1) % 10)
#             q_list1 = "".join(q_list_minus)
#             self.percombination(q_list1, deadends, target, level + 1)

#     def openLock(self, deadends: List[str], target: str) -> int:

#         self.percombination("0000", deadends, target, 0)

#         return self.possiblelevels


# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         # if deadends == "0000" end
#         # create queue
#         queue = ["0000"]
#         level = 0
#         size = len(queue)

#         while queue:

#             level += 1

#             for i in range(size):
#                 q = queue.pop(0)
#                 q_list = list(q)
#                 q_list_plus, q_list_minus = q_list, q_list

#                 for i in range(4):
#                     # update each q
#                     q_list_plus[i] = str((int(q_list[i]) + 1) % 9)
#                     q_list0 = "".join(q_list_plus)
#                     q_list_minus[i] = str((int(q_list[i]) - 1) % 9)
#                     q_list1 = "".join(q_list_minus)

#                     queue.append(q_list0)
#                     queue.append(q_list1)

#             queue = list(set(queue) - set(deadends))
#             size = len(queue)

#             if q in target:

#                 return level
