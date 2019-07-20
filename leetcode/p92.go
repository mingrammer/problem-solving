package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	hnode := head
	var tail *ListNode
	for i := 0; i < m-1; i++ {
		if i == m-2 {
			tail = head
		}
		head = head.Next
	}
	var rev, revTail *ListNode
	for i := 0; i < n-m+1; i++ {
		rev = &ListNode{
			Val:  head.Val,
			Next: rev,
		}
		if i == 0 {
			revTail = rev
		}
		head = head.Next
	}
	revTail.Next = head
	if tail == nil {
		return rev
	}
	tail.Next = rev
	return hnode
}
