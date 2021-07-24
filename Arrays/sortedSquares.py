from typing import List

# import heapq


def sortedSquares(nums: List[int]) -> List[int]:
    pos_list = [i ** 2 for i in nums if i >= 0]
    neg_list = [i ** 2 for i in nums if i < 0]
    neg_list.reverse()

    # return list(heapq.merge(pos_list, neg_list))

    res = []
    neg_ind = 0
    for val in pos_list:
        while neg_ind < len(neg_list) and neg_list[neg_ind] <= val:
            res.append(neg_list[neg_ind])
            neg_ind += 1
        res.append(val)

    res.extend(neg_list[neg_ind:])

    return res


print(sortedSquares([-4, -2, 0, 3, 4, 10]))


def sortedSquares2(nums: List[int]) -> List[int]:
    res = []
    left = next(
        (i for i in range(0, len(nums) - 1) if abs(nums[i]) < abs(nums[i + 1])),
        len(nums) - 1,
    )
    right = left + 1
    while left >= 0 or right < len(nums):
        if right >= len(nums) or (left >= 0 and abs(nums[left]) < abs(nums[right])):
            res.append(nums[left] ** 2)
            left -= 1
        else:
            res.append(nums[right] ** 2)
            right += 1
    return res
