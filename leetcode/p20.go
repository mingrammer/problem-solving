package main

type stack struct {
	base []rune
	top  int
}

func (s *stack) push(r rune) {
	s.base[s.top] = r
	s.top++
}

func (s *stack) pop() rune {
	s.top--
	return s.base[s.top]
}

func (s *stack) empty() bool {
	return s.top == 0
}

func isValid(s string) bool {
	ps := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}
	st := &stack{
		base: make([]rune, len(s)),
		top:  0,
	}
	for _, r := range s {
		switch r {
		case '(', '{', '[':
			st.push(r)
		case ')', '}', ']':
			p := ps[r]
			if st.empty() || (st.pop() != p) {
				return false
			}
		}
	}
	return st.empty()
}
