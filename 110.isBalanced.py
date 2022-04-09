from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min = 0
        self.max = 0
    def heightBTFunc(self, node, c):
        if not node:
            print(c)
            self.min = min(c, self.min)            
            self.max = max(c, self.max)
            return 
    
        self.heightBTFunc(node.left, c + 1)
        self.heightBTFunc(node.right, c + 1)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.heightBTFunc(root, 0)
        print(self.max, self.min)
        return (self.max - self.min) <= 1 

    