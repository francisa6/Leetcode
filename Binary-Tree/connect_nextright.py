# The question is a bit misleading. You can connect a N.right to N.left it's not all rights.

# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class SolutionRecursive:
    # def nextrightnode(self, node: "Node") -> "Node":
    #     # stop when node.right or node.next is not null
    #     while node and (node.right is None and node.next):
    #         node = node.next
    #     return node

    # def nextptrnode(self, node: "Node") -> "Node":
    #     # can be none
    #     while node.left is None and node.right is None and node.next:
    #         if node.left:
    #             return node.left
    #         if node.right:
    #             return node.right
    #         node = node.next
    #     return node

    # def connect(self, root: "Node") -> "Node":
    #     if not root or (root.left is None and root.right is None and root.next is None):
    #         return root

    #     # is not none
    #     start_ptr = self.nextptrnode(root)
    #     ptr = start_ptr
    #     # can be none
    #     ptrfast = self.nextrightnode(root)

    #     # find the starting node in level
    #     while ptrfast and ptr:
    #         ptr.next = ptrfast.right
    #         ptrfast = self.nextrightnode(ptrfast.next)
    #         ptr = self.nextptrnode(ptr.next)

    #     # Next level
    #     self.connect(start_ptr)

    def nextrightnode(self, root: "Node") -> "Node":
        # TopLevelPtr is the top node and BottomLevelPtr is the next level node ptr
        TopLevelPtr = root
        # create a dummy node with dummy.next as the starting node of the next level

        while TopLevelPtr:

            dummy = BottomLevelPtr = Node(0)

            while TopLevelPtr:
                if TopLevelPtr.left:
                    BottomLevelPtr.next = TopLevelPtr.left
                    BottomLevelPtr = BottomLevelPtr.next

                if TopLevelPtr.right:
                    BottomLevelPtr.next = TopLevelPtr.right
                    BottomLevelPtr = BottomLevelPtr.next

                # Keep iterating over the top level until null
                TopLevelPtr = TopLevelPtr.next

            # Need to reset TopLevelPtr pointer to the start of next (bottom) level
            TopLevelPtr = dummy.next

        return root
