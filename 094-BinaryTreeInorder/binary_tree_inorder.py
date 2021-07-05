# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):

        ## recursive version

        # result = []
        # if root.left is not None:
        #     result += self.inorderTraversal(root.left)
        # if root.val is not None:
        #     result += [root.val]
        # if root.right is not None:
        #     result += self.inorderTraversal(root.right)
        # return result

        # stack version: less informative
        result = []
        stack = []
        while root is not None or len(stack)>0:
            while root is not None:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            if root.val is not None:
                result.append(root.val)
            root = root.right
