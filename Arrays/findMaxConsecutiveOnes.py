# Max consecutive Ones
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    maxcounter = 0
    counter = 0
    for val in nums:
        counter = counter + 1 if val == 1 else 0
        if counter > maxcounter:
            maxcounter = counter
 

    return maxcounter


findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])


