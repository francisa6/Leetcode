from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TOO complicated solution
class SolutionComplicated:
    # Removed the Optional[TreeNode] in onePathSum -- the input is always not none in onePathSum
    # SOMETIMES IT IS USEFUL TO MAKE THE SUBFUNCTION NOT ALLOW NONE FOR THE RECURSIVE STEP!
    def onePathSum(self, root: TreeNode, accum: int, targetSum: int) -> bool:
        accum += root.val
        if (root.left is None) and (root.right is None) and accum == targetSum:
            return True
        elif (root.left is None) and (root.right is None) and accum != targetSum:
            return False

        left_found = root.left and self.onePathSum(root.left, accum, targetSum)
        right_found = root.right and self.onePathSum(root.right, accum, targetSum)
        return left_found or right_found

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        else:
            accum = 0
            return self.onePathSum(root, accum, targetSum)


class SolutionNotSoClean:
    # Not as clean as below because we have to add in  + root.left.val etc.
    def onePathSum(self, root: Optional[TreeNode], accum: int, targetSum: int) -> bool:
        if root is None:
            return False
        if (root.left is None) and (root.right is None) and accum == targetSum:
            return True
        return self.onePathSum(
            root.left, accum + root.left.val, targetSum
        ) or self.onePathSum(root.right, accum + root.right.val, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.onePathSum(root, root.val, targetSum)


class Solution:
    def onePathSum(self, root: Optional[TreeNode], accum: int, targetSum: int) -> bool:
        if root is None:
            return False
        accum += root.val
        if (root.left is None) and (root.right is None) and accum == targetSum:
            return True
        return self.onePathSum(root.left, accum, targetSum) or self.onePathSum(
            root.right, accum, targetSum
        )

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.onePathSum(root, 0, targetSum)


# Test tree
node0 = TreeNode(3)
node1 = TreeNode(9)
node0.left = node1
node2 = TreeNode(5)
node1.left = node2
node3 = TreeNode(20)
node0.right = node3
node4 = TreeNode(15)
node3.left = node4
node5 = TreeNode(7)
node3.right = node5

print("Solution: ", Solution().hasPathSum(node0, 10))
