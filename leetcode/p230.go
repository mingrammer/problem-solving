package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func traverse(root *TreeNode) []int {
	order := []int{}
	if root.Left != nil {
		order = append(order, traverse(root.Left)...)
	}
	order = append(order, root.Val)
	if root.Right != nil {
		order = append(order, traverse(root.Right)...)
	}
	return order
}

func kthSmallest(root *TreeNode, k int) int {
	return traverse(root)[k-1]
}
