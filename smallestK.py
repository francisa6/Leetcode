"""
time complex for add is O(log(k)) and for getsmallest it is O(k) but only because Python doesn't have max heap easily and
for smallestK it is O(nlog(k))
space complex is O(k)

"""

from dataclasses import dataclass
from heapq import heappush, heappop
from typing import List


class RunningSmallestK:
    def __init__(self, k: int):
        self.k = k
        self.smallestK = []  # loop invariance: length <= k before and after you add()

    def add(self, num: int) -> None:
        # if the largest element in smallestK > num then remove and add nums
        heappush(self.smallestK, -num)

        if len(self.smallestK) > self.k:
            heappop(self.smallestK)

    # Out of all nums added so far, return the smallest k in any order
    # Time complexity: O(k)
    def getSmallestK(self) -> List[int]:
        return [-i for i in self.smallestK]


# Give me the smallest k numbers from nums


# O(n*log(k)) time complexity
def smallestK(nums: List[int], k: int) -> List[int]:
    runningSmallest = RunningSmallestK(k)
    for n in nums:
        runningSmallest.add(n)

    return runningSmallest.getSmallestK()


@dataclass
class Point:
    x: int
    y: int

    # we can actually redefine lt to make it a max heap
    # by using '>' in my_distance > other_distance.
    # We could have defined it as a min heap by using
    # '<' in my_distance < other_distance.

    def __lt__(self, other: "Point") -> bool:
        my_distance = self.x ** 2 + self.y ** 2
        other_distance = other.x ** 2 + other.y ** 2
        return my_distance > other_distance


class RunningSmallestK:
    def __init__(self, k: int):
        self.k = k
        self.smallestK = []  # loop invariance: length <= k before and after you add()

    def add(self, point: Point) -> None:
        # if the largest element in smallestK > num then remove and add nums
        heappush(self.smallestK, point)

        if len(self.smallestK) > self.k:
            heappop(self.smallestK)

        point1 = Point()
        point2 = Point()

    # Out of all nums added so far, return the smallest k in any order
    # Time complexity: O(k)
    def getSmallestK(self) -> List[Point]:
        return self.smallestK
