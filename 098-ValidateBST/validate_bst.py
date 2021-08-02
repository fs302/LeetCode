# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(root, lower, upper):
            # case-1: Root is NULL
            if root is None:
                return True
            # case-2: Value Exception
            if root.val >= upper or root.val <= lower:
                return False
            status = True
            # case-3: Subtree Test
            if root.left is not None:
                left = root.left
                status = status & check(left, lower, root.val)
            if root.right is not None:
                right = root.right
                status = status & check(right, root.val, upper)
            return status
        return check(root, float(-inf), float(inf))