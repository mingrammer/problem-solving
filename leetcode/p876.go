package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	var i, j int
	middle := head
	for head != nil && head.Next != nil {
		head = head.Next
		i++
		if j*2 < i {
			middle = middle.Next
			j++
		}
	}
	return middle
}
