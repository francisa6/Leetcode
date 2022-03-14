# Space complexity would be O(height of tree) and Time complexity O(height of tree)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionSmart:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
            
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root



class SolutionSlow:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.insertIntoBSTSub(root, root, val)

    def insertIntoBSTSub(self, root, currNode, val):
        if not currNode:
            return TreeNode(val)

        if currNode.val < val:
            if currNode.right is None:
                currNode.right = TreeNode(val)
                return root
            return self.insertIntoBSTSub(root, currNode.right, val)
            
        if currNode.val > val:
            if currNode.left is None:
                currNode.left = TreeNode(val)
                return root
            return self.insertIntoBSTSub(root, currNode.left, val)


