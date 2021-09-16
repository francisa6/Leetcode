from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Recursively compute by node
    def swapPairsSub(self, prevNode: ListNode, head: Optional[ListNode]):
        if head is None or head.next is None:
            return
        else:
            prevNode.next = head.next
            head.next = prevNode.next.next
            prevNode.next.next = head

            return self.swapPairsSub(head, head.next)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = ListNode(next=head)
        self.swapPairsSub(prevNode, head)
        return prevNode.next


class SolutionShorter:
    # Recursively compute by row
    # Recognise that if we have the previous row we can get the next row
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
