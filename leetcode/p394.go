package main

import (
	"strconv"
	"strings"
)

type stack struct {
	top  int
	vals []string
}

func newStack(n int) *stack {
	return &stack{-1, make([]string, n)}
}

func (st *stack) push(s string) {
	st.top++
	st.vals[st.top] = s
}

func (st *stack) pop() string {
	s := st.vals[st.top]
	st.top--
	return s
}

func (st *stack) isEmpty() bool {
	return st.top == -1
}

func decodeString(s string) string {
	st := newStack(len(s))
	var n int
	for _, b := range s {
		switch {
		case b == ']':
			var p string
			for {
				v := st.pop()
				if v == "[" {
					n, _ := strconv.Atoi(st.pop())
					st.push(strings.Repeat(p, n))
					break
				}
				p = v + p
			}
		case b >= 48 && b <= 57:
			n = 10*n + int(b-48)
		default:
			if n > 0 {
				st.push(strconv.Itoa(n))
				n = 0
			}
			st.push(string(b))
		}
	}
	var ds string
	for !st.isEmpty() {
		ds = st.pop() + ds
	}
	return ds
}
