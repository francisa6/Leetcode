# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional


class Solution:
    # Tail recursive solution
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        preHead = ListNode(val = 0)

        def mergeTwoListsSub(prev, l1, l2, counter) -> Optional[ListNode]:
            # Base
            if (not l1 and not l2) or counter > 0:
                return preHead.next
            
            if not l1 or not l2:
                counter +=1
            
            if not l1 or (l2 and l2.val <= l1.val):
                prev.next = l2
                return mergeTwoListsSub(prev.next, l1, l2.next, counter)

            if not l2 or (l1 and l1.val < l2.val):
                prev.next = l1
                return mergeTwoListsSub(prev.next, l1.next, l2, counter)

        return mergeTwoListsSub(preHead, l1, l2, 0)

class Solution2:
    # Is not tail recursive because we are continually building a call stack and we need to trace back to the starting node
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        if l2.val < l1.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        