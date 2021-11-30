/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	root_val := preorder[0]
	var node TreeNode
	node.Val = root_val
	if len(preorder) == 1 {
		return &node
	}
	pos := findIndex(inorder, root_val)
	left_inorder := inorder[:pos]
	right_inorder := inorder[pos+1:]
	left_len := len(left_inorder)
	node.Left = buildTree(preorder[1:left_len+1], left_inorder)
	node.Right = buildTree(preorder[left_len+1:], right_inorder)
	return &node
}

func findIndex(list []int, target int) (index int) {
	for i := 0; i < len(list); i++ {
		if target == list[i] {
			return i
		}
	}
	return -1
}