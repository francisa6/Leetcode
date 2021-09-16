from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = None
for i in reversed([1, 2]):
    node = ListNode(i, head)
    head = node


def to_list(node: ListNode):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


print("true head", to_list(head))

# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/discuss/64501/Java-easy-to-understand
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the length of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is denotes the beginning of the second list
        # reverse send part of list
        acc2 = None
        head2 = slow

        while head2:
            nextnode2 = head2.next

            head2.next = acc2
            acc2 = head2
            head2 = nextnode2

        # print("acc2", to_list(acc2))
        # print("head", to_list(head))

        # acc2 will always be longer than the first list
        while acc2:
            if acc2.val != head.val:
                return False

            acc2 = acc2.next
            head = head.next

        return True


print(Solution().isPalindrome(head))


# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         # Find the length of the list
#         head_copy = head
#         i = 0
#         while head_copy is not None:
#             head_copy = head_copy.next
#             i += 1

#         startPal = i // 2
#         # print("startPal", startPal)

#         # Find the start of the second list
#         # beglist2 is the memory address for the start of the 2nd list
#         beglist2 = head
#         i = 0
#         while i < startPal:
#             beglist2 = beglist2.next
#             i += 1

#         # print("beglist2.val", beglist2.val)
#         # reverse send part of list
#         acc2 = None
#         head2 = beglist2

#         while head2 != None:
#             nextnode2 = head2.next

#             head2.next = acc2
#             acc2 = head2
#             head2 = nextnode2

#         # print("acc2", to_list(acc2))
#         # print("head", to_list(head))

#         i = 0
#         while i <= startPal - 1:
#             if acc2.val != head.val:
#                 return False

#             acc2 = acc2.next
#             head = head.next
#             i += 1

#         return True


# print(Solution().isPalindrome(head))
