from typing import List

[1, 2, 6, 2, 3, 5]  # upper bound can be 7

# arr is an array of integers where all of them are nonnegative and less than or equal to maximum.
# maximum will be some small constant between 1 and 1000 and generally less than len(arr).
# Sort the array in-place. You can use extra storage. But the algorithm must be O(n).
def sortSmallNumbers(arr: List[int], maximum: int):
    count_arr = [0] * (maximum + 1)

    for val in arr:
        count_arr[val] += 1  # runs n=len(arr) times
    k = 0
    for j in range(len(count_arr)):
        # runs len(count_arr) = maximum+1 times
        for _ in range(count_arr[j]):
            # This runs count_arr[0] + ... + count_arr[-1] = n times in total across the entire outer loop too
            arr[k] = j
            k += 1
    # Total time is n + n = 2n. Here we don't care about the k because k <<n.


# But if max is allowed to vary independently of n and it is also really really big then we might have 2n+k times.
# Then we should have something like O(n+k)
