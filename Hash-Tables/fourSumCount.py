import collections

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        Map0 = {s: [(i)] for i, s in enumerate(nums1)}

        for nums in [nums2, nums3, nums4]:
            
            Map1 = {}

            for key, list_tuples in Map0.items():
                for i, s in enumerate(nums):
                    new_key = key + s
                    new_list_tuples = [tuple_i + (i) for tuple_i in list_tuples]

                    if new_key in Map1.keys():
                        # append to existing list
                        new_list_tuples = Map1[new_key] + new_list_tuples 
                    
                    Map1[new_key] = new_list_tuples
                        
                    
            Map0 = Map1
        return len(Map0[0])

class SolutionCount:        
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        Map0 = {0: 1}

        for nums in [nums1, nums2, nums3, nums4]:
            
            Map1 = {}

            for key, num_tuples in Map0.items():
                for s in nums:
                    new_key = key + s
                    new_num_tuples = num_tuples

                    if new_key in Map1.keys():
                        # append to existing list
                        new_num_tuples = Map1[new_key] + new_num_tuples 
                    
                    Map1[new_key] = new_num_tuples
                        
                    
            Map0 = Map1
        return Map0[0]
            
    
    def fourSumCountFast(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = collections.Counter(a + b for a in nums1 for b in nums2)
        AB[-2]
        return sum([AB[-c-d] for c in nums3 for d in nums4])


