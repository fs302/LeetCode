# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        results = []
        queue = []
        queue.append((root, 0))
        
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if depth >= len(results):
                results.append([])
            if depth % 2 == 0:
                results[depth].append(node.val)
            else:
                results[depth].insert(0, node.val)
            if node.left is not None:
                queue.append((node.left, depth+1))
            if node.right is not None:
                queue.append((node.right, depth+1))
        
        return results