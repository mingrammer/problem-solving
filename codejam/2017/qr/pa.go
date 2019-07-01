package main

import (
	"fmt"
	"strings"
)

func flip(c byte) byte {
	if c == '-' {
		return '+'
	}
	return '-'
}

func solve() int {
	_s, _n := "", 0
	fmt.Scanf("%s %d\n", &_s, &_n)
	b, n := []byte(_s), len(_s)
	i, c := 0, 0
	for i < n {
		if b[i] == '-' {
			if i+_n > n {
				break
			}
			for j := i; j < i+_n; j++ {
				b[j] = flip(b[j])
			}
			c++
		}
		i++
	}
	s := string(b)
	if strings.Contains(s, "-") {
		return -1
	}
	return c
}

func main() {
	var _t int
	fmt.Scanln(&_t)
	for c := 0; c < _t; c++ {
		ans := solve()
		if ans < 0 {
			fmt.Printf("Case #%d: %v\n", c+1, "IMPOSSIBLE")
		} else {
			fmt.Printf("Case #%d: %v\n", c+1, ans)
		}
	}
}
