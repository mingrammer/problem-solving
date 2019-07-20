package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var rev *ListNode
	for head != nil {
		rev = &ListNode{
			Val:  head.Val,
			Next: rev,
		}
		head = head.Next
	}
	return rev
}
