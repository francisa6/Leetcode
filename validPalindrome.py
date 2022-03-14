class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        def dfs(l, r, counter = 0):
            if counter <= 1 and l >= r:
                return True
            elif counter > 1:
                return False
            else:
                if s[l] != s[r]:
                    return dfs(l+1, r, counter+1) or dfs(l, r-1, counter+1)
                else:
                    return dfs(l+1, r-1, counter)
        
        return dfs(l, r, 0)

s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
# s = "abcca"
print(Solution().validPalindrome(s))
