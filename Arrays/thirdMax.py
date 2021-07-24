from typing import List


# def thirdMax(nums: List[int]) -> int:
#     if len(nums) < 4:
#         return max(nums)
#     else:
#         i = 0
#         prev_max = max(nums)
#         while i < len(nums) - 1:

#             if nums[i] < prev_max:
#                 next_max = max([nums[i], next_max])
#             i += 1

#         prev_max = next_max


def thirdMax(nums: List[int]) -> int:

    l2, l1, l = (-(2 ** 31)) - 1, (-(2 ** 31)) - 1, nums[0]

    for val in nums[1:]:
        if val > l:
            l2, l1, l = l1, l, val

        elif l1 < val < l:
            l2, l1 = l1, val

        elif l2 < val < l1:
            l2 = val

    if l2 == (-(2 ** 31)) - 1:
        l2 = l
    return l2


arr = [1, 2]
print(thirdMax(arr))
