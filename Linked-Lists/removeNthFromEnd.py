# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        ptr, ptr_lagn = head, head
        i = 0
        while ptr is not None:
            ptr = ptr.next

            if i > n:
                ptr_lagn = ptr_lagn.next
            i += 1
            print(i)

        if head.next == None:
            head = None
        elif n == 1:
            ptr_lagn.next = None
        elif n == i:
            head = head.next
        else:
            ptr_lagn.next = ptr_lagn.next.next

        return head


# Add a dummy node at the front to deal with asymmetry caused by head!
# Try to write the solution in such a way that there is not a lot of indices because it can
# get confusing.The below is much better because it splits up the while loop above into 2
# separate steps. This is done in 2N time <=> to O(N).
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre_head = ListNode(0, head)
        ptr, ptr_lagn = pre_head, pre_head
        for _ in range(n):
            ptr = ptr.next
        while ptr.next is not None:
            ptr = ptr.next
            ptr_lagn = ptr_lagn.next
        ptr_lagn.next = ptr_lagn.next.next
        return pre_head.next


# Note we don't do ptr_lagn.next because ptr_lagn gives you the memory address of the node we are interested in

head = None

for i in reversed([1, 2, 3, 4, 5]):
    node = ListNode(i)
    node.next = head
    head = node


def to_list(node: ListNode):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


print(to_list(Solution2().removeNthFromEnd(head, 1)))
