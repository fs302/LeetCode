/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if root.Left == nil && root.Right == nil {
		return 1
	}
	lv := maxDepth(root.Left)
	rv := maxDepth(root.Right)
	res := lv
	if lv < rv {
		res = rv
	}
	return res + 1
}
