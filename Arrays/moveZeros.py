from typing import List

# def moveZeros(nums: List[int]) -> None:
#     r = -1
#     for w in range(len(nums)):

#         while r < len(nums) - 1:
#             r += 1

#             if nums[r] != 0:
#                 print(r)
#                 break
#         if r < len(nums):
#             nums[w] = nums[r]
#             if r == len(nums) - 1:
#                 r += 1
#         else:
#             nums[w] = 0


def moveZeros(nums: List[int]) -> None:
    if len(nums) > 1:
        w = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[w] = nums[r]
                w += 1

        for i in range(w, len(nums)):
            nums[i] = 0


arr = [0, 1, 0, 3, 12]
moveZeros(arr)
print(arr)
