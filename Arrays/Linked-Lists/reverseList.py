# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == None:
            return head

        org_head = head

        while org_head.next is not None:
            post_head = org_head.next
            post_post_head = post_head.next

            new_head = post_head
            new_head.next = head
            head = new_head

            org_head.next = post_post_head

        return head


class Solution2:
    # Iterative version of the recursive reverse function
    # This is not in place. It allocates new nodes.
    def reverseList(self, head: ListNode) -> ListNode:
        accResult = None
        while head is not None:
            accResult = ListNode(head.val, accResult)
            head = head.next
        return accResult


class Solution3:
    # in place version of Solution2. It does not allocate new nodes.
    # Instead it is reversing the arrows (the next pointers).
    def reverseList(self, head: ListNode) -> ListNode:
        accResult = None
        while head is not None:
            nextHead = head.next
            head.next = accResult
            accResult = head
            head = nextHead
        return accResult
