# O(max(N1, N2)) tc and O(N1)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = {}, {}
        
        for n1 in nums1:
            dict1[n1] = dict1[n1] + 1 if n1 in dict1 else 1
        
        for n2 in nums2:
            if n2 in dict1:
                dict2[n2] = dict2[n2] + 1 if n2 in dict2 else 1

        final_list = []
        for key in dict2.keys():
            for _ in range(min(dict1[key], dict2[key])):
                final_list.append(key)
        return final_list

    def instersectLessMemory(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        res = []

        for n1 in nums1:
            dict1[n1] = dict1.get(n1, 0) + 1
        
        for n2 in nums2:
            if n2 in dict1 and dict1[n2] > 0:
                res.append(n2)
                dict1[n2] -= 1
        return res