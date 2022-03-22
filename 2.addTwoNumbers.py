# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        res = head
        carry = 0
        
        while l1 or l2 or carry > 0:
            sval = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + carry
            
            carry, digit = sval // 10, sval % 10 
            
            res.next = ListNode(val=digit)
            res = res.next
            
            l1 = l1.next if l1 is not None else None            
            l2 = l2.next if l2 is not None else None

        return head.next