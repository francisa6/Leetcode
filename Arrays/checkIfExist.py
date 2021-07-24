from typing import List


def checkIfExist(arr: List[int]) -> bool:

    for i, arr_i in enumerate(arr):
        for arr_j in arr[i + 1 :]:
            if arr_i == arr_j * 2 or arr_i * 2 == arr_j:
                return True
    return False


res = checkIfExist([14, 1, 7, 11])
print(res)
