package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	next := new(ListNode)
	l3 := next
	var n, carry int
	for {
		n = carry
		if l1 != nil {
			n += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			n += l2.Val
			l2 = l2.Next
		}
		carry = n / 10
		next.Val = n % 10
		if l1 == nil && l2 == nil && carry == 0 {
			break
		}
		next.Next = new(ListNode)
		next = next.Next
	}
	return l3
}
