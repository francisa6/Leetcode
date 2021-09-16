# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = None
for i in reversed([1, 2, 3, 4]):
    nextlist = ListNode(i, head)
    head = nextlist


def to_list(head):
    results = []
    temp_head = head
    while temp_head is not None:
        results.append(temp_head.val)
        temp_head = temp_head.next
    return results


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         temp_head = head
#         while head != None and head.next != None:
#             new_head = head.next
#             if head.next.next != None:
#                 head.next = head.next.next
#             else:
#                 head.next = None

#             new_head.next = temp_head
#             temp_head = new_head
#         return temp_head


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        accResults = None
        while head is not None:
            nexthead = head.next
            head.next = accResults
            accResults = head
            head = nexthead

print(to_list(Solution().reverseList(head)))
