from typing import Callable, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fromList(values: List[int]) -> ListNode:
    head = None
    for i in reversed(values):
        node = ListNode(i)
        node.next = head
        head = node
    return head


def toList(node: ListNode):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def exists(head: ListNode, target: int) -> bool:
    if head is None:
        return False
    else:
        if head.val == target:
            return True
        return exists(head.next, target)


def map(head: ListNode, fn: Callable[[int], int]) -> ListNode:
    if head is None:
        return None
    else:
        return ListNode(fn(head.val), map(head.next, fn))


# print(toList(map(fromList([1,2,3,4]), lambda x: x * 2)))


# revAppend
def reverseHelper(head: ListNode, accResult: ListNode) -> ListNode:
    if head is None:
        return accResult
    else:
        return reverseHelper(head.next, ListNode(head.val, accResult))


def reverse(head: ListNode) -> ListNode:
    return reverseHelper(head, None)

def merge(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    else:
        if list1.val < list2.val:
            return ListNode(list1.val, merge(list1.next, list2))
        else:
            return ListNode(list2.val, merge(list1, list2.next))

print(toList(reverse(fromList([1, 2, 3, 4]))))
