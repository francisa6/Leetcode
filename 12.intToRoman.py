"""
O(n) time and O(n) space. The first sol requires less time
than encoding because you have to through len of roman which is longer.
"""


class Solution:
    """
    1s digit to 10s digit to 100s etc.
    """

    def intToRoman(self, num: int) -> str:
        roman = {0: "", 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        res = ""
        unit = 1

        while (num // unit) > 0:

            n = ((num // unit) % 10) * unit

            if n in roman:
                res = roman[n] + res
            elif (n + unit) in roman:
                res = roman[unit] + roman[n + unit] + res
            elif n // (5 * unit) > 0:
                res = roman[5 * unit] + roman[unit] * ((n - 5 * unit) // unit) + res
            else:
                res = roman[unit] * (n // unit) + res

            unit *= 10

        return res


class Solution2:
    """
    100s then 10s then 1s etc.
    """

    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        res, i = "", 0

        # stops when num = 0
        while num:
            res += (num // values[i]) * numerals[i]
            num = num % values[i]
            i += 1

        return res
