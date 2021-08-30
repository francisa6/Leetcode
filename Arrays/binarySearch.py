from typing import List, Optional


# Return index of target in arr if found. Return None if not found.
def binarySearchRecursive(arr: List[int], target: int) -> Optional[int]:
    def recursion(left: int, right: int) -> Optional[int]:
        if left > right:
            return None
        middle = left + (right - left) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            return recursion(middle + 1, right)
        else:
            return recursion(left, middle - 1)

    return recursion(0, len(arr) - 1)


# Return index of target in arr if found. Return None if not found.
# Time complexity: O(log(n))
# Space complexity: O(1)
def binarySearch(arr: List[int], target: int) -> Optional[int]:
    # get middle value

    left = 0
    right = len(arr) - 1
    while True:

        middle = left + (right - left) // 2

        # left and right index to choose the value
        if target > arr[middle]:
            # choose left block
            left = middle + 1

        elif target == arr[middle]:
            return middle
        else:
            right = middle - 1


arr = [-50, 20, 30, 31, 40, 99, 100]
index = binarySearch(arr, 40)
# Should be 4
print("binarySearch(arr, 40) =", index)
