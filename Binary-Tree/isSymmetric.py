from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric2Nodes(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None) != (q is None):
            return False

        return (
            p.val == q.val
            and self.isSymmetric2Nodes(p.left, q.right)
            and self.isSymmetric2Nodes(p.right, q.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.isSymmetric2Nodes(root.left, root.right)


class SolutionCleaner:
    def isSymmetric2Nodes(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) or (q is None):
            return (p is None) == (q is None)

        return (
            p.val == q.val
            and self.isSymmetric2Nodes(p.left, q.right)
            and self.isSymmetric2Nodes(p.right, q.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root is None or self.isSymmetric2Nodes(root.left, root.right)


# Test tree
node0 = TreeNode(3)
node1 = TreeNode(9)
node0.left = node1
node3 = TreeNode(20)
node0.right = node3
node4 = TreeNode(15)
node3.left = node4

print("Solution: ", Solution().isSymmetric(node0))
