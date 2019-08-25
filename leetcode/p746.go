package main

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minCostClimbingStairs(cost []int) int {
	n := len(cost)
	for i := 2; i < n; i++ {
		cost[i] += min(cost[i-2], cost[i-1])
	}
	return min(cost[n-2], cost[n-1])
}
