from typing import List

[1, 2, 6, 2, 3, 5]  # upper bound can be 7

# arr is an array of integers where all of them are nonnegative and less than or equal to maximum.
# maximum will be between 1 and 1000.
# Sort the array in-place. You can use extra storage. But the algorithm must be O(n).
def sortSmallNumbers(arr: List[int], maximum: int):
    count_arr = [0] * (maximum + 1)

    for val in arr:
        count_arr[val] += 1
    k = 0
    for j in range(len(count_arr)):
        for _ in range(count_arr[j]):
            arr[k] = j
            k += 1
