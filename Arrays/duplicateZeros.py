from typing import List


# def duplicateZeros(arr: List[int]) -> None:
#     s = 0
#     e = 0
#     i = 1
#     prev_s = -1

#     if arr[0] == 0:
#         s = 0
#     while i < len(arr):
#         if arr[i - 1] != 0 and arr[i] == 0:
#             s = i

#         elif arr[i - 1] == 0 and arr[i] != 0 and prev_s != s:
#             e = i
#             carry_arr = arr[s : e ].copy()
#             arr[i : i + (e - s)] = carry_arr

#             num_zero_replace = min([e - s , len(arr) - i])

#             arr[s : e ] = [0] * num_zero_replace
#             i = i + e - s - 1
#             print(i, arr, num_zero_replace, s, e, carry_arr)
#             prev_s = s
#         i += 1


def duplicateZeros(arr: List[int]) -> None:
    n_zero = 0
    i = 0
    while i + n_zero < len(arr):
        
        if arr[i] == 0:
            n_zero += 1
        i += 1
    for k in range(i - 1, -1, -1):
        val = arr[k]
        if k + n_zero < len(arr):
            arr[k + n_zero] = val
        if val == 0:
            n_zero -= 1
            arr[k + n_zero] = 0


arr1 = [1, 0, 2, 3]
duplicateZeros(arr1)
print(arr1)
