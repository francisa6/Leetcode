from typing import List


def removeElement(nums: List[int], val: int) -> int:
# k num of values returned
    k = 0
    for i in range(len(nums)):

        if nums[i] != val :
            if i != k: nums[k] = nums[i] 
            k +=1
            
    return k

nums = [0,1,2,2,3,0,4,2]
val = 2


val1 = removeElement(nums, val)
print(val1)
print(nums)