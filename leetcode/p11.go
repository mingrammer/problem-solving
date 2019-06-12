package main

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxArea(height []int) int {
	m := 0
	l, r := 0, len(height)-1
	for l < r {
		area := (r - l) * min(height[l], height[r])
		if area > m {
			m = area
		}
		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}
	return m
}
