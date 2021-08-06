# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # case-1: p,q are None
        if p is None and q is None:
            return True
        # case-2: p,q are valid
        if p is not None and q is not None:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        # case-3: one of p,q is None
        return False