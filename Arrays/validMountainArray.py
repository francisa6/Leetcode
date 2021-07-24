from typing import List


# def validMountainArray(arr: List[int]) -> bool:
# if len(arr) < 3:
#     return False
# else:

#     post_ind = True
#     if arr[0] >= arr[1] or arr[-2] <= arr[-1]:
#         return False
#     prev_val = arr[1]
#     for val in arr[2:]:

#         if val < prev_val:
#             post_ind = False

#         if (val > prev_val and not post_ind) or val == prev_val:
#             return False

#         prev_val = val

#     return True


# def validMountainArray(arr: List[int]) -> bool:
#     if len(arr) < 3 or arr[0] >= arr[1] or arr[-2] <= arr[-1]:
#         return False
#     else:
#         prev_val2, prev_val1 = arr[0], arr[1]

#         for val in arr[2:]:
#             if (
#                 (prev_val2 == prev_val1)
#                 or (prev_val1 == val)
#                 or (prev_val2 >= prev_val1 and prev_val1 <= val)
#             ):
#                 return False

#             prev_val2 = prev_val1
#             prev_val1 = val
#         return True


def validMountainArray(arr: List[int]) -> bool:

    start = 0

    n = len(arr) - 1
    end = n - 1
    while start != n and arr[start] < arr[start + 1]:
        start += 1
    while end != 0 and arr[end - 1] > arr[end]:
        end -= 1

    return start == end and end != n - 1 and start != 0


arr = [3, 2, 4, 6, 5, 5, 2]
print(validMountainArray(arr))
