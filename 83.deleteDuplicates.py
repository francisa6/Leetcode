# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lNode = head
        rNode = head
        
        while rNode:
            
            if lNode.val != rNode.val:
                lNode.next = rNode
                lNode = rNode
            
            rNode = rNode.next
        
        if lNode:
            lNode.next = None 
        
        return head

class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lNode = head

        while lNode and lNode.next:
            if lNode.val == lNode.next.val:
                lNode.next = lNode.next.next
            else:
                lNode = lNode.next

        return head