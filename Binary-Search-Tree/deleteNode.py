# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class SolutionSmart:
    # https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1006/discuss/213685/Clean-Python-3-with-comments-in-details
    # Idea is to search for root.left most right node (can also search of root.right most left node) and use that value to replace the root.

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        if root.val == key:
            # Try to iterate through the left
            # no left
            if not root.left:
                return root.right
            else:

                # at least 1 left
                newNode = root.left
                while newNode.right:
                    newNode = newNode.right
                # swap newNode with root
                root.val = newNode.val

                # Now we want to delete the val that we replaced!
                root.left = self.deleteNode(root.left, newNode.val)

        elif root.val < key:
            # parent node of deleted node will also fall into these conditions
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root


class SolutionNaive:
    # Idea is to search for root.right most left node and use that value to replace the root. I should have just done replacement
    # by replacing the val of the node instead of actually swapping the node! Also don't need as many cases as listed below

    def swapNode(self, prenewNode, newNode, keyNode):
        keyNode_oldleft, keyNode_oldright = keyNode.left, keyNode.right
        prenewNode.left = prenewNode.left.right
        newNode.left, newNode.right = keyNode_oldleft, keyNode_oldright
        return newNode

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        if root.val == key:
            # Case 2: 2 child
            if root.left and root.right:
                newNode = root.right

                if not newNode.left:
                    root.right.left = root.left
                else:
                    while newNode.left:
                        prenewNode = newNode
                        newNode = newNode.left
                        # swap newNode with root
                    newNode = self.swapNode(prenewNode, newNode, root)
                return newNode

            elif not root.left and not root.right:
                # Case 3: no child
                return None
            else:
                # Case 1: 1 child
                return root.right or root.left

        elif root.val < key:
            # parent node of deleted node will also fall into these conditions
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root
