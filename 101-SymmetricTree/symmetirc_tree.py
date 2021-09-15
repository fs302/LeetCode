# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 不是特别高效的实现，相比官方方法多了不少空间消耗
    def travel(self, root, direction, depth, child_type=0):
        if root == None:
            return []
        res = []
        l_res = self.travel(root.left, direction, depth+1, 0)
        r_res = self.travel(root.right, direction, depth+1, 1)
        # 为了区别不同层的同数字节点，以 0 为底进行乘倍
        # 为了区别左右子树，对方向和子树类别进行异或
        if direction == 0:
            res = l_res + [2 * (child_type^direction) + root.val + 2 * depth] + r_res # 左子树优先
        else:
            res = r_res + [2 * (child_type^direction) + root.val + 2 * depth] + l_res # 右子树优先
        return res
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        left_travel = self.travel(root.left, 0, 0, 0)
        right_travel = self.travel(root.right, 1, 0, 1)
        # print(left_travel)
        # print(right_travel)
        if len(left_travel) != len(right_travel):
            return False
        for v1,v2 in zip(left_travel, right_travel):
            if v1 != v2:
                return False
        return True
        