from typing import List

"""
Note that we don't have to consider the case where l_i - 1 and r_i + 1 because these cases are already considered 
as we start from l_i, r_i = 0, len(numbers) - 1 which is the max and min values of these variables.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_i, r_i = 0, len(numbers) - 1
        while l_i < r_i:
            SumVal = numbers[l_i] + numbers[r_i]
            if SumVal == target:
                return [l_i + 1, r_i + 1] 
            elif SumVal < target:
                l_i += 1
            else:
                r_i -= 1 

class SolutionRecusive:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_numbers = len(numbers)
        def twoSumSub(l_i, r_i):

            if 0 <= l_i < r_i < len_numbers:
                SumVal = numbers[l_i] + numbers[r_i]

                if SumVal == target:
                    res.append([l_i + 1, r_i + 1])
                    return 
                elif SumVal > target:
                    twoSumSub(l_i, r_i - 1)
                else:
                    twoSumSub(l_i + 1, r_i)

        res = []
        twoSumSub(0, len_numbers - 1)
        return res[0]

numbers = [2,7,11,15] 
target = 9

print(Solution().twoSum(numbers, target))
# print(SolutionRecusive().twoSum(numbers, target))


