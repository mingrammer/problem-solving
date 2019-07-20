package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var rev *ListNode
	cur := head
	for head != nil {
		head = head.Next
		cur.Next = rev
		rev = cur
		cur = head
	}
	return rev
}
