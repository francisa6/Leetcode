from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        arr[-1] = -1
    elif len(arr) > 1:

        max_i = arr[-1]
        last_i = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):

            max_i = max([max_i, last_i])
            last_i = arr[i]
            arr[i] = max_i
    return arr

arr = [17,18,5,4,6,1]
res = replaceElements(arr)
print(res)
