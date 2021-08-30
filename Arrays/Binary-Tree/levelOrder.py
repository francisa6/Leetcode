from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative Solutions
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node = []
        child = []
        results = []

        if root:
            node.append(root)

        while node or child:
            level = []

            while node:
                # This pop(0) is important because otherwise we will be getting the wrong order
                x = node.pop(0)
                level.append(x.val)
                if x.left:
                    child.append(x.left)
                if x.right:
                    child.append(x.right)
            results.append(level)
            node, child = child, node

        return results

    def levelOrder_shorter(self, root: Optional[TreeNode]) -> List[List[int]]:
        node = []
        child = []
        results = []

        if root:
            node.append(root)

        while node:
            results.append([leaf.val for leaf in node])
            child = []
            for leaf in node:
                child.extend([leaf.left, leaf.right])
            # remove the Nones to get the node for the next iteration and store val
            node = [leaf for leaf in child if leaf]

        return results

    def levelOrder_shorter2(self, root: Optional[TreeNode]) -> List[List[int]]:
        node = []
        results = []

        if root:
            node.append(root)

        while node:
            results.append([leaf.val for leaf in node])
            child = [(leaf.left, leaf.right) for leaf in node]
            # remove the Nones to get the node for the next iteration and store val
            node = [leaf for leaftuple in child for leaf in leaftuple if leaf]

        return results

    def levelOrder_shorter3(self, root: Optional[TreeNode]) -> List[List[int]]:
        node = []
        results = []

        if root:
            node.append(root)

        while node:
            results.append([leaf.val for leaf in node])
            # remove the Nones to get the node for the next iteration and store val
            node = [
                leaf
                for leaftuple in node
                for leaf in (leaftuple.left, leaftuple.right)
                if leaf
            ]

        return results


class SolutionRecusive:
    def __init__(self):
        self.res = []

    def horizontal_level(self, root: Optional[TreeNode], level):
        if not root:
            return []

        if level < len(self.res):
            self.res[level].append(root.val)
        else:
            self.res.append([root.val])
        print(self.res)
        self.horizontal_level(root.left, level + 1)
        self.horizontal_level(root.right, level + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.horizontal_level(root, 0)
        return self.res


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

print("Solution: ", Solution().levelOrder(root))

print("Solution: ", SolutionRecusive().levelOrder(root))
