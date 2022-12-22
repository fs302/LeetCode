# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.best = -1001
    
    def singleMaxSum(self, root: Optional[TreeNode]) -> int:
        # 明修栈道：计算以 root 节点为根的单向最大路径和
        if root is None:
            return 0

        leftMax = max(self.singleMaxSum(root.left), 0)
        rightMax = max(self.singleMaxSum(root.right), 0)

        # 暗度陈仓：更新全局的双向最大路径和
        combineMax = root.val + leftMax + rightMax
        if combineMax > self.best:
            self.best = combineMax

        return root.val + max(leftMax, 
                              rightMax, 
                              0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.singleMaxSum(root)
        return self.best
