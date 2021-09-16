# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

rightNode = TreeNode(-1)
tree = TreeNode(val= 0, right= rightNode)

# Note that 'if 0:' is the same as 'if None:' !!!!!! Becareful!
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTSub(root, min, max):
            # Check
            if not root:
                return True

            if min is not None and root.val <= min:
                return False
                
            if max is not None and root.val >= max:
                return False

            # Otherwise continue checking
            return isValidBSTSub(root.left, min, root.val) and \
                isValidBSTSub(root.right, root.val, max)

        return isValidBSTSub(root, None, None)
        

# Use -inf and inf to make it shorter
class SolutionShorter:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTSub(root, min, max):
            # Check
            if not root:
                return True

            if  root.val <= min or root.val >= max:
                return False

            # Otherwise continue checking
            return isValidBSTSub(root.left, min, root.val) and \
                isValidBSTSub(root.right, root.val, max)

        return isValidBSTSub(root, float('-inf'), float('inf') )



print(SolutionShorter().isValidBST(tree))
print('Solution should be',  False)