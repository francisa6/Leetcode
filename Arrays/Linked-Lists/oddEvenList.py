from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head):
    results = []
    while head is not None:
        results.append(head.val)
        head = head.next
    return results


# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/discuss/133345/With-detailed-explanation-or-Python
# this solution is better than mine
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        odd, even = head, head.next
        start_even = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = start_even
        return head


# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:

#         preNode = ListNode(0, head)
#         slow, fast = preNode, preNode.next

#         while fast and fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next

#             begeven = slow.next
#             slow.next = fast.next
#             fast.next = fast.next.next
#             slow.next.next = begeven

#         return preNode.next


head = None
for i in reversed([1, 2, 3, 4, 5]):
    tempnode = ListNode(i, head)
    head = tempnode


print(to_list(head))
print(to_list(Solution().oddEvenList(head)))
print("Done")
