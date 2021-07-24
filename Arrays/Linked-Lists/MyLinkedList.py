# Single Linked List

# Define what a node looks like! It has two attributes a value and a reference to the next node
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.xyz = 1234


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initalise the linked list. It has head equals to None value and has length zero!
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # Can the index be neg?

        if self.size - 1 < index or self.size == 0 or index < 0:
            return -1
        else:
            # set the first node to be the head node
            # What happens when index = 0? does it access the next current_node.next?

            current_node = self.head
            if self.size > 1:
                for _ in range(index):
                    current_node = current_node.next

            return current_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.size == 0:
            self.head = Node(val)
        else:
            current_node = self.head
            for _ in range(1, self.size):
                current_node = current_node.next
            current_node.next = Node(val)

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            pass
        else:

            if index == 0:
                self.addAtHead(val)
            else:
                # index equal to length or less than
                current_node = self.head

                for _ in range(index - 1):
                    current_node = current_node.next

                current_node.next = Node(val)
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            curr_node = self.head
            self.head = curr_node.next

        if index > 0 and index <= self.size - 1:
            curr_node = self.head
            for _ in range(1, index):
                curr_node = curr_node.next
            # index node -1 should be the last curr_node
            # How to store a whole node in?
            curr_node.next = curr_node.next.next

            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
