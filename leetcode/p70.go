package main

var steps = map[int]int{}

func climbStairs(n int) int {
	if n < 3 {
		return n
	}
	if m, ok := steps[n]; ok {
		return m
	}
	steps[n] = climbStairs(n-1) + climbStairs(n-2)
	return steps[n]
}
