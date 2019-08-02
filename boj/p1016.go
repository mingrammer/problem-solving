package main

import (
	"fmt"
	"math"
)

func main() {
	var min, max int
	fmt.Scanln(&min, &max)
	msqrt := int(math.Sqrt(float64(max)))
	sieve := make([]bool, max-min+1)
	for i := 2; i <= msqrt; i++ {
		s := i * i
		for j := min; j <= max; {
			if j%s == 0 {
				sieve[j-min] = true
				j += s
			} else {
				j += (s - j%s)
			}
		}
	}
	cnt := 0
	for _, ok := range sieve {
		if !ok {
			cnt++
		}
	}
	fmt.Println(cnt)
}
