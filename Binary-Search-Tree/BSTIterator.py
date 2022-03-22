# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Complexity: amortized time complexity of next function is O(1): 
# we spend O(n) time to visit all n nodes. Note, that amortized time means, 
# that we spend O(1) in average, it is exactly what we need in follow-up. 
# Also space complexity for this solution is O(h): our stack will never be 
# longer than height of our tree.

# Instead of a stack we can solve this using a parent node to save time and space.
# Ask WJ how parent node saves time?

class BSTIteratorClean:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.stackAllLeft(root)

    def stackAllLeft(self, Node):
        currNode = Node
        while currNode:
            self.stack.append(currNode)
            currNode = currNode.left

    def next(self) -> int:

        returnNode = self.stack.pop()

        # Update stack
        # Check if right branch exists if it does then collect all Left Nodes
        # Max number of elements stored is the height of the tree
        if returnNode.right:
            self.stackAllLeft(returnNode.right)

        return returnNode.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()