from sys import set_asyncgen_hooks


# class Solution:
#     def printReverse(self, s):
#         if len(s) == 0:
#             return ""

#         else:
#             return s[-1] + self.printReverse(s[:-1])


# print(Solution().printReverse("abcwer"))


class Solution:
    def reverseStringSub(self, s, i):
        # print(i, s)
        if (len(s) - 1 - i) <= i:
            return s
        else:
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
            return self.reverseStringSub(s, i + 1)

    def reverseString(self, s):
        return self.reverseStringSub(s, 0)


# s = ["h", "e", "l", "l", "o"]
s = ["H", "a", "3", "n", "a", "h"]
# s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]


print(Solution().reverseString(s))
