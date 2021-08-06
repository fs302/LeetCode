# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # using stack to store temp nodes
        stack = []
        x = y = pre = None
        while (len(stack) > 0 or root is not None):
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # condition: find two nodes in wrong place
            #            root is smaller value, pre is larger value
            # case-1, pos(root) = pos(pre) + 1, then only swap neighbors
            # case-2, pos(root) > pos(pre) + 1, then swap new root and old pre
            if pre is not None and pre.val > root.val:
                y = root 
                if x is None:
                    x = pre
                else:
                    break
            pre = root
            root = root.right 
        if x is not None and y is not None:
            tmp = x.val
            x.val = y.val
            y.val = tmp

