from typing import List


def findNumbers(nums: List[int]) -> int:
    counter = 0
    for val in nums:
        if len(str(val)) % 2 == 0:
            counter = counter + 1 
    return counter


findNumbers([12,345,2,6,7896])
