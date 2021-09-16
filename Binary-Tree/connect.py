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


class Solution:
    def connect(self, root: "Node") -> "Node":
        Q = []

        if root:
            Q.append(root)

        while Q and Q[0].left:

            # Make the connections
            for i in range(len(Q)):
                current_Q = Q[i]
                # connect left and right nodes
                current_Q.left.next = current_Q.right

                if i + 1 < len(Q):
                    next_Q = Q[i + 1]
                    current_Q.right.next = next_Q.left

            # Define next level
            Q = [leaf for l in Q for leaf in [l.left, l.right] if leaf]

        return root


class SolutionRecursive:
    def connect(self, root: "Node") -> "Node":
        if not root.left:
            return root

        root.left.next = root.right
        print("connected: ", root.left.val, root.right.val)

        if root.next:
            root.right.next = root.next.left
            print("connected: ", root.right.val, root.next.left.val)

        self.connect(root.left)
        self.connect(root.right)
