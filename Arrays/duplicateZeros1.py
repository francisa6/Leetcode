from typing import List


def dupzero(arr: List[int]) -> List[int]:
    j = -1
    i = 0
    while i < len(arr):
        if arr[j+ 1] == 0:
            i += 2
        else:
            i += 1
        j += 1
    print(j)
    # j is the last index desired
    ind = len(arr)-1
    for k in range(j, -1, -1):

        if arr[k] == 0:

            arr[ind] = 0

            ind -=1


arr1c = [1, 0, 2]
dupzero(arr1c)
print(arr1c)