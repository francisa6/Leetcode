# O(2*N1 + N2) approx. O(N1 + N2) time complexity (do we need to include 'in' lookup, which is on average O(1) complexity? NO. and similarly for min? NO as constant time complexity) and space complexity is 
# O(N1 + constant) approx. O(N1) space complexity 

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        threshold = len(list1) + len(list2) + 1
        list1dict = {key: e for e, key in enumerate(list1)}

        for e2, key2 in enumerate(list2):
            if key2 in list1dict.keys():
                list1dict[key2] += e2 + threshold

        min_index = min([val for val in list1dict.values() if val >= threshold])
        return [key for key, val in list1dict.items() if val == min_index]
 
# ["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
# ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]