from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        stack = []
        if root:
            stack.append(root)

        while stack:
            x = stack.pop()
            if isinstance(x, int):
                path.append(x)

            else:
                if x.right:
                    stack.append(x.right)
                stack.append(x.val)
                if x.left:
                    stack.append(x.left)

        return path


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
            if root
            else []
        )
