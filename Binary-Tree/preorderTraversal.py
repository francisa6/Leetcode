from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# inputlist = [1,2,3]
# def listtotree(inputlist):
#     i = 0
#     while True:
#         newnode = TreeNode(inputlist[i], left= inputlist[i+1], right= inputlist[i+2])


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # define the result "path"
        path = []
        # define a call stack - we use this to determine the intermediate results
        stack = []
        if root:
            stack.append(root)

        while stack:
            x = stack.pop()
            if isinstance(x, int):
                path.append(x)

            else:
                # We need to write this backwards i.e. for preorder traversal it should be NLR
                if x.right:
                    stack.append(x.right)
                if x.left:
                    stack.append(x.left)
                # Note this has to be a value it can't be a memory address otherwise the if isinstance part detect it
                stack.append(x.val)

        return path


class SolutionRecursive:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base case
        if not root:
            return []

        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.result


class SolutionRecursive2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
            if root
            else []
        )


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
root = node0

solutionrecursive = SolutionRecursive().preorderTraversal(root)
print("Solution: ", solutionrecursive)

solutionrecursive = SolutionRecursive2().preorderTraversal(root)
print("Solution: ", solutionrecursive)
