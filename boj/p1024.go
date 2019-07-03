package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	var n, l float64
	fmt.Scanln(&n, &l)
	for k := l; ; k++ {
		if k > 100 {
			fmt.Print(-1)
			break
		}
		m := n/k - (k-1)/2
		if m < 0 {
			fmt.Print(-1)
			break
		}
		c := math.Floor(m)
		if c == m {
			a := []string{}
			for i := m; i < m+k; i++ {
				a = append(a, strconv.Itoa(int(i)))
			}
			fmt.Print(strings.Join(a, " "))
			break
		}
	}
}
