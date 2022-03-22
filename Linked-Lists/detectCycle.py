# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# If I know there is a cycle then we can find the periodicity
# Then we start again from node 0, node 1 etc. and for each we run it for the period.
# If after the period length it doesn't hit the same value then it is not the pos value


# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:

#         # Check if node and find the period if there is a cycle
#         ptr = head
#         ptr2 = head
#         period_count = 0
#         period = 0
#         while True:

#             if ptr == None or (ptr2 == None or ptr2.next == None):
#                 return

#             if ptr == ptr2:
#                 if period_count == 0:
#                     period = 0
#                 period_count += 10000000000000
#                 if period_count == 2:
#                     break

#             ptr = ptr.next
#             ptr2 = ptr2.next.next
#             period += 1

#         # Run from the start of the list and check each value until it stops

#         pos = -1
#         while True:
#             pos += 1

#             store_address = head
#             for _ in range(pos):
#                 store_address = store_address.next

#             check_pos = store_address
#             for _ in range(period - 1):
#                 check_pos = check_pos.next

#             if check_pos.next == store_address:
#                 return check_pos.next


# [3, 2, 0, -4]
# 1

from typing import Pattern


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ptr = head
        ptr2 = head
        while ptr is not None and ptr2 is not None and ptr2.next is not None:
            ptr = ptr.next
            ptr2 = ptr2.next.next
            if ptr == ptr2:
                while head != ptr:
                    head = head.next
                    ptr = ptr.next
                return head
        return None


head = None

for i in reversed([3, 2, 0, -4]):
    node = ListNode(i)
    node.next = head
    head = node

head.next.next.next.next = head.next

print(Solution().detectCycle(head).val)
