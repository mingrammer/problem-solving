package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// recursion.
// func reverseList(head *ListNode) *ListNode {
// 	if head == nil || head.Next == nil {
// 		return head
// 	}
// 	tail := reverseList(head.Next)
// 	head.Next.Next = head
// 	head.Next = nil
// 	return tail
// }

// iteration.
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
