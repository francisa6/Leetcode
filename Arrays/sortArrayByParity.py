from typing import List


# def sortArrayByParity(nums: List[int]) -> List[int]:
#     count_even = 0
#     for i in nums:
#         if i % 2 == 0:
#             count_even += 1
#     print(count_even)
#     if count_even == len(nums) or count_even == 0:
#         return nums
#     else:
#         # count_even = start odd

#         odd = count_even
#         j = 0
#         for e in range(count_even):
#             if nums[e] % 2 == 1:

#                 while nums[odd + j] % 2 != 0:
#                     j += 1
#                 nums[e], nums[odd + j] = nums[odd + j], nums[e]
#                 j += 1
#         return nums


def sortArrayByParity(nums: List[int]) -> List[int]:

    # count_even = start odd

    j = len(nums) - 1

    for e in range(len(nums)):

        if nums[e] % 2 == 1:

            while nums[j] % 2 != 0 and e < j:
                j -= 1
            nums[e], nums[j] = nums[j], nums[e]
            j -= 1
        if e >= j:
            break

    return nums


nums = [0, 1, 3]
res = sortArrayByParity(nums)
print(res)
