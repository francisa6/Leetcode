class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()

        for key in nums:
            if key in numsSet:
                return True
            numsSet.add(key)
        
        return False

def containsDuplicateFast(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))