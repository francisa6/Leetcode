from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2Pointers:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        currNode = root
        while currNode:
            prevNode = currNode
            if currNode.val < val:
                currNode = currNode.right
                if not currNode:
                    prevNode.right = TreeNode(val)
            else:
                currNode = currNode.left
                if not currNode:
                    prevNode.left = TreeNode(val)

        return root

class Solution1Pointer:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
            
        currNode = root
        while True:
            if currNode.val < val:
                if currNode.right:
                    currNode = currNode.right
                else: 
                    currNode.right = TreeNode(val)
                    break
            else:
                if currNode.left:
                    currNode = currNode.left
                else: 
                    currNode.left = TreeNode(val)
                    break
        return root