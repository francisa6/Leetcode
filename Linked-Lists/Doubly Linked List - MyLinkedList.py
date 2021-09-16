## Doubly Linked List
from typing import List


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the
        end of linked list. If index is greater than the length, the node will not be inserted.
        """

        curr = self.head
        if index == self.size:
            # append end
            for _ in range(index - 1):
                curr = curr.next
            if self.size == 0:
                self.head = Node(val, curr)
            else:
                curr.next = Node(val, curr)

            self.size += 1
        elif index < self.size:
            for _ in range(index):
                curr = curr.next

            newNode = Node(val, curr.prev, curr)

            if index == 0:
                self.head.prev = newNode
                self.head = newNode
            else:
                curr.prev.next = newNode
                curr.prev = newNode

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < self.size:

            curr = self.head

            if index == 0:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
            else:
                for _ in range(index):
                    curr = curr.next

                prev_node = curr.prev
                prev_node.next = curr.next
                if curr.next is not None:
                    curr.next.prev = prev_node
            self.size -= 1
