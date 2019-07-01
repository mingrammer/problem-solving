package main

import (
	"fmt"
)

func solve() string {
	_s := ""
	fmt.Scanf("%s\n", &_s)
	b, n := []byte(_s), len(_s)
	for i := 0; i < n-1; i++ {
		if b[i] > b[i+1] {
			j := i
			for j > 0 && b[j] == b[j-1] {
				j--
			}
			b[j]--
			for k := j + 1; k < n; k++ {
				b[k] = 57
			}
			break
		}
	}
	if b[0] == 48 {
		b = b[1:]
	}
	return string(b)
}

func main() {
	var _t int
	fmt.Scanln(&_t)
	for c := 0; c < _t; c++ {
		ans := solve()
		fmt.Printf("Case #%d: %v\n", c+1, ans)
	}
}
