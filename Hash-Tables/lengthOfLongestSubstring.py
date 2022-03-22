
# If we only wanted to have one max(curr_max, xxx) statement we can
# just update curr_max after each loop iteration but that will be more 
# expensive as there are unnecessarily updates being made.

# Space O(distinct s letters, symbols etc) and time O(len(s)) 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_max = 0
        lagptr = 0
        hashmap = {}
        for currptr, l in enumerate(s):
            if l in hashmap and lagptr <= hashmap[l]:
                #update new value
                curr_max = max(curr_max, currptr - lagptr )
                lagptr = hashmap[l] + 1

            hashmap[l]=currptr 
            
        return max(curr_max, len(s) - lagptr)    