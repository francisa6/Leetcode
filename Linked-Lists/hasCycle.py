# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ptr = head
        ptr2 = head
        while ptr is not None and ptr2 is not None and ptr2.next is not None:
            # Remember that the order of the above conditions matter! think about the cases when there is 0, 1, 2 elements
            # the check looks at whether the current or next steps are going to give you None
            # It's called short circuiting.
            # Remember not to add in special cases
            ptr = ptr.next
            ptr2 = ptr2.next.next
            if ptr == ptr2:
                return True
        return False
