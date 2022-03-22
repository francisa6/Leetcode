from typing import List


# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     if m == 1 and n == 1:
#         nums1 = nums2
#     elif m > 1 and n > 0:
#         for val2 in nums2:
#             i = 0
#             while True:
#                 if nums1[i] < val2 and val2 <= nums1[i + 1]:
#                     nums1[i + 2 :] = nums1[i + 1 : -1]
#                     nums1[i + 1] = val2
#                     break
#                 if i == m - 1:
#                     nums1[m - 1] = val2
#                 i += 1


# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     # ind - full list
#     # m - nums1
#     # n - nums2
#     if n > 0:
#         for ind in range(m + n - 1, -1, -1):
#             if max([nums1[m - 1], nums2[n - 1]]) == nums2[n - 1] and m > 0:
#                 nums1[ind] = nums2[n - 1]
#                 n -= 1
#                 if n == 0:
#                     break
#             elif m > 0:
#                 nums1[ind] = nums1[m - 1]
#                 m -= 1
#             else:
#                 nums1[ind] = nums2[n - 1]
#                 n -= 1


# Time complexity O(m + n)
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # ind - full list
    # m - nums1
    # n - nums2
    if n > 0:
        for ind in range(m + n - 1, -1, -1):
            if m == 0 or (m > 0 and max([nums1[m - 1], nums2[n - 1]]) == nums2[n - 1]):
                nums1[ind] = nums2[n - 1]
                n -= 1
                if n == 0:
                    break
            else:
                nums1[ind] = nums1[m - 1]
                m -= 1


nums2 = [1]
n = len(nums2)
nums1 = [2, 0]
m = len(nums1) - len(nums2)

merge(nums1, m, nums2, n)
print(nums1)
