from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Bottom-up approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution2:
    def __init__(self):
        self.answer = 0

    # Top-down approach
    def maxDepth(self, root: Optional[TreeNode], depth):
        print(root)
        # Base case
        if root is None:
            print("hi", self.answer)
            return 

        # Find the maximum depth by comparing each of the max depths for
        # each possible path down the tree. 'depth' denotes the currently
        # active path
        if root.left is None and root.right is None:
            self.answer = max(self.answer, depth)
            print("answer: ", self.answer)
            # print("root val ", root.val)

        # Contructs all the possible paths down the tree possible by going
        # left and right
        self.maxDepth(root.left, depth + 1)
        self.maxDepth(root.right, depth + 1)



node0 = TreeNode(3)
node1 = TreeNode(9)
node0.left = node1
node3 = TreeNode(20)
node0.right = node3
node4 = TreeNode(15)
node3.left = node4

# print("Solution: ", Solution().maxDepth(node0))

Sol2 = Solution2()
Sol2.maxDepth(node0, 1)
print("Solution2: ", Sol2.answer)
