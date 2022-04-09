from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.height = []
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def minDepthSub(root, c):
            if not root.left and not root.right:
                self.height.append(c)
                return 
            if root.left:
                minDepthSub(root.left, c + 1)
            if root.right:
                minDepthSub(root.right, c + 1)
        
        if not root:
            return 0
        minDepthSub(root, 1)
        return min(self.height) 