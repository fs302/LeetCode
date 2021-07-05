from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def generateBst(self, st, ed) -> List[TreeNode]:
        if st > ed:
            return [None]
        if st == ed:
            root = TreeNode()
            root.val = st 
            return [root]
        result = []
        for i in range(st, ed+1):
            left_choice = self.generateBst(st, i-1)
            right_choice = self.generateBst(i+1, ed)
            for left in left_choice:
                for right in right_choice:
                    root = TreeNode()
                    root.val = i 
                    root.left = left 
                    root.right = right 
                    result.append(root)
        return result

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateBst(1, n)