# Definition for singly-linked list.
# Remember that when deleting or altering nodes in any way I need to reason about
# the .next and see if it is doing exactly what I want it to! e.g. in this case
# make sure that the curr.next didn't skip over the checking of the val of the curr.next
# node after deleting!


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # prenode
        prenode = ListNode(0, head)
        curr = prenode
        while curr.next is not None:

            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return prenode.next


# Recursive solution
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        else:
            if head.val == val:
                return self.removeElements(head.next, val)
            else:
                return ListNode(head.val, self.removeElements(head.next, val))
