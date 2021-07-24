from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    for val_ind in nums:
        val = val_ind if val_ind <= n else val_ind - n
        if nums[val - 1] <= n:
            nums[val - 1] += n

    missing_nums = []
    for i in range(len(nums)):
        if nums[i] <= n:
            missing_nums.append(i + 1)
    return missing_nums


def findDisappearedNumbers2(nums: List[int]) -> List[int]:
    for val_ind in nums:
        val = abs(val_ind)
        nums[val - 1] = -abs(nums[val - 1])

    missing_nums = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing_nums.append(i + 1)
    return missing_nums


arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(arr))
