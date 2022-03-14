# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRecursive:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True

        elif not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
class SolutionRecursiveNeat:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

class SolutionRecursiveNeat1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def t(n):
            print(n and (n.val, t(n.left), t(n.right)))
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)

class SolutionRecursiveNeat2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Base case
        if not p and not q:
            return True
        elif not p or not q:
            return False

        p_queue = [p]
        q_queue = [q]

        while len(p_queue) > 0 or len(q_queue) > 0:
            # Need 'or' for p_queue shorter than q_queue vv.
            p_curr = p_queue.pop(0)
            q_curr = q_queue.pop(0)
            
            if p_curr == q_curr == None:
                continue
                
            # if not equal in val then return False
            if (not p_curr or not q_curr) or \
                (p_curr.val != q_curr.val):
                return False
        
            p_queue.extend([p_curr.left, p_curr.right])
            q_queue.extend([q_curr.left, q_curr.right])
            
        return True 
