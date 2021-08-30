# Going through the while loops is 2N then going through thte second while
# loop is N so in total it is 3N. Therefore it is O(N) time.

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def listLen(self, head: ListNode) -> int:
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        num_nodesA = self.listLen(headA)
        num_nodesB = self.listLen(headB)
        if num_nodesA < num_nodesB:
            num_nodesA, num_nodesB = num_nodesB, num_nodesA
            headA, headB = headB, headA
        for _ in range(num_nodesA - num_nodesB):
            headA = headA.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


# head = None

# for i in reversed([3, 2, 0, -4]):
#     node = ListNode(i)
#     node.next = head
#     head = node

# head.next.next.next.next = head.next

# print(Solution().detectCycle(head).val)
