"""

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
        
class Solution1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxEdges = 0
        
        def depth(root):
            if not root:
                return 0
            depthL = depth(root.left)
            depthR = depth(root.right)
            self.maxEdges = max(self.maxEdges, depthL + depthR)
            return max(depthL, depthR) + 1
        
        _ = depth(root)
        return self.maxEdges




# class WRONGSolution:
#     def __init__(self):
#         self.maxEdges = 0
        
#     def maxEdgesBT(self, root):
#         if not root:
#             return 0
#         return max(self.maxEdgesBT(root.left), self.maxEdgesBT(root.right)) + 1

#     def diameterOfBinaryTreeSub(self, root: Optional[TreeNode]) -> None:
#         if not root:
#             return 
#         self.maxEdges = max(self.maxEdges, self.maxEdgesBT(root.left) + self.maxEdgesBT(root.right))
        
#         self.diameterOfBinaryTreeSub(root.left)                                   
#         self.diameterOfBinaryTreeSub(root.right)

#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.diameterOfBinaryTreeSub(root)
#         return self.maxEdges 