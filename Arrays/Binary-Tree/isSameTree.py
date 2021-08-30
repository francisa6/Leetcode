# https://leetcode.com/problems/same-tree/discuss/32729/Shortest%2Bsimplest-Python


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Cases
        if p is None and q is None:
            return True
        # if (p is None and q is not None) or (p is not None and q is None):
        #     return False
        if (p is None) != (q is None):
            return False

        # Statment that summarises truth for all paths of the tree
        # When we don't have a null
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
