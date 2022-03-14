from typing import List


def binarySearch_v1(array: List[int], target: int):
    l, r = 0, len(array) - 1
    while l <= r:
        mid = l + (r - l) // 2  # same as (l + r) // 2 

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def binarySearch_different_index(array: List[int], target: int):
    l, r = 0, len(array) 
    while l < r:
        mid = l + (r - l) // 2 

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            r = mid 
        else:
            l = mid + 1
    return -1


array = [1,2,3,4] 
target = 5
print(binarySearch_v1(array, target))
print(binarySearch_different_index(array, target))