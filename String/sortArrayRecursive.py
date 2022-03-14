from typing import List
import random


class Solution:
    def mergeArray(self, acc_nums, curr_nums):
        acc_nums_new = [0] * (len(acc_nums) + len(curr_nums))
        acc_i, curr_i = 0, 0
        for i in range(len(acc_nums_new)):
            if (curr_i > len(curr_nums) - 1) or (
                acc_i <= len(acc_nums) - 1 and acc_nums[acc_i] < curr_nums[curr_i]
            ):
                acc_nums_new[i] = acc_nums[acc_i]
                acc_i += 1
            else:
                acc_nums_new[i] = curr_nums[curr_i]
                curr_i += 1
        return acc_nums_new

    def sortArrayRecursive(self, acc_nums, list_nums) -> List[int]:
        if not list_nums:
            print("acc_nums", acc_nums)
            return acc_nums

        curr_nums = list_nums.pop(0)

        if len(curr_nums) != 1:
            if curr_nums[0] > curr_nums[1]:
                curr_nums[0], curr_nums[1] = curr_nums[1], curr_nums[0]

        # merge acc_nums and curr_nums
        print("acc_nums", acc_nums, "curr_nums", curr_nums)
        acc_nums_new = self.mergeArray(acc_nums, curr_nums)
        return self.sortArrayRecursive(acc_nums_new, list_nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        list_nums = [
            nums[2 * n_i : 2 * n_i + 2] for n_i in range(len(nums) // 2 + len(nums) % 2)
        ]
        return self.sortArrayRecursive([], list_nums)


# test = Solution()
# acc_nums = [2, 5]
# curr_nums = [3]
# sortedarray = test.mergeArray(acc_nums, curr_nums)

# print('sortedarray', sortedarray)

# nums = [5,1,1,2,0,0]
# test.sortArray(nums)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:

            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid:]
            # print(r)

            l = self.sortArray(l)
            r = self.sortArray(r)

            i, j, k = 0, 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[k] = l[i]
                    i += 1

                else:
                    nums[k] = r[j]
                    j += 1
                k += 1

            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1
            # print('nums', nums, l, r)
        return nums

    def quicksort(self, nums: List[int]) -> List[int]:
        # Runtime: O(nlogn) expected, O(n^2) worst case.
        # With a proper choice of pivot (using the median of medians algorithm), the runtime can be reduced to strict O(nlogn).
        # Space: O(n) expected, O(n^2) worst case
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        l = [v for v in nums if v < pivot]
        e = [v for v in nums if v == pivot]
        r = [v for v in nums if v > pivot]

        return self.quicksort(l) + e + self.quicksort(r)


test = Solution()
nums = [5, 3, 1]
print(test.sortArray(nums))
print(test.quicksort(nums))
