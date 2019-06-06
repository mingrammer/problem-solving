package main

import (
	"math"
)

func reverse(x int) int {
	p := int(math.Abs(float64(x)))
	n := int(math.Log10(float64(p)))
	r := 0
	for i := n; i >= 0; i-- {
		r += (p % 10) * int(math.Pow10(i))
		p /= 10
	}
	if r < math.MinInt32 || r > math.MaxInt32 {
		return 0
	}
	if x < 0 {
		return -r
	}
	return r
}
