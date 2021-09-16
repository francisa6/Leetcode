class Node:
    def __init__(self, node_val):
        self.val = node_val
        self.next = None  # reference


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None  # ptr a node
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1

        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
            # the first ptr.next gives you 1st node ref. So we need (i-1)th node as that contains the ith reference
        return ptr.val  # get the ith val from the (i-1)th pointer

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
        if index <= self.size:
            if index == 0:
                node = Node(val)
                node.next = self.head
                self.head = node
            else:
                ptr = self.head
                for _ in range(index - 1):
                    ptr = ptr.next
                node = Node(val)
                node.next = ptr.next
                ptr.next = node

            # replace the (i-1)th next with a new pointer to Node containing val
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < self.size:
            ptr = self.head

            if index == 0:

                self.head = ptr.next
            else:

                for _ in range(index - 1):
                    ptr = ptr.next
                    # gives you the ith index ref

                ptr.next = ptr.next.next
                # index-2 th node'ts next/ith minus 1 reference
                # if index =2 and self.size = 3 then ptr.next.next= None so it's fine
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# index = 0
# param_1 = obj.get(index)
# val = 2
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)
