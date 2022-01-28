from typing import List

class Solution0:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + carry == 10:
                digits[i] = 0
                carry = 1
                if i == 0:
                    digits = [1] + digits
                    return digits
            else:
                digits[i] += carry
                return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            new_num = digits[i] + carry
            carry = new_num // 10
            if carry > 0:
                digits[i] = new_num % 10
                if i == 0 and carry > 0:
                    digits.insert(0, carry)
                    return digits
            else:
                digits[i] += 1
                return digits

digits = [9,9]
print(Solution().plusOne(digits))