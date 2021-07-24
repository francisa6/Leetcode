from typing import List

# Space complexity =1 (as inplace) and time complexity is N (as one loop)


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        k = 0
    else:
        k = 1
        last_used_val = nums[0]
        for val in nums:
            if val != last_used_val:
                nums[k] = val
                last_used_val = val
                k += 1

    return k


nums = nums = []
k = removeDuplicates(nums)
print(k, nums)
