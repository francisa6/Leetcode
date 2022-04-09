"""
time O(n)
space O(n)
"""
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Find the count of each of the tasks
        d = {}
        for t in tasks:
            d[t] = d.get(t, 0) + 1

        # use the task that has the most number of repeats as
        # a frame to structure the schedule. For example if
        # n=2 and tasks=["A", "A", "A", "B", "B", "B"] then
        # ["A", ..., "A", ...,  "A"] and then fill in using the
        # remaining tasks. In this case we would fill in with "B".
        maxRepeats = max(d.values())

        # covers the case when there are multiple tasks that
        # have the same number of repeats.
        countMaxRepeats = sum(maxRepeats == v for v in d.values())

        # First term defines a block ["A", ...] in
        # ["A", ..., "A", ...] and last term is the last ["A"]
        # which doesn't have terms thereafter unless it's a task
        # that has repeats = max repeat.
        # The term (n + 1) * (maxRepeats - 1) covers the
        # case: ["A", "B", "A", "C", "A"]
        totalNSub = (n + 1) * (maxRepeats - 1) + countMaxRepeats

        # The case when n < # unique letters. We need to slip
        # these back in. E.g. ["A", "B", "C", "A", "B", "A"]
        adj = max(0, len(tasks) - totalNSub)

        return totalNSub + adj


from collections import Counter


class SolutionShorter:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counts = Counter(tasks).values()
        max_count = max(tasks_counts)
        repeats_max_count = list(tasks_counts).count(max_count)
        return max(len(tasks), (n + 1) * (max_count - 1) + repeats_max_count)


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

print(SolutionShorter().leastInterval(tasks, n))
