class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            i_val = digits[i] + carry

            if i_val > 9:
                i_val_list = str(i_val)
                carry = int(i_val_list[0])
                i_val = int(i_val_list[1])
                digits[i] = i_val

                if i == 0:
                    return [carry] + digits
            else:
                digits[i] = i_val
                return digits

