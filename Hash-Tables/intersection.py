# Needs O(1)? space complexity (for the intersection) and O(len(nums1)) time complexity 

class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        intersectionList = []

        for n1 in nums1Set:
            if n1 in nums2Set:
                intersectionList.append(n1)

        return intersectionList

    def intersectionFaster(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))