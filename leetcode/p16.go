package main

import (
	"math"
	"sort"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func threeSumClosest(nums []int, target int) int {
	c := math.MaxInt32
	n := len(nums)
	if n < 3 {
		return nums[0] + nums[1] + nums[2]
	}
	sort.Ints(nums)
	for i, e := range nums {
		if i > 0 && e == nums[i-1] {
			continue
		}
		l, r := i+1, n-1
		for l < r {
			for l > i+1 && l < n-2 && nums[l] == nums[l-1] {
				l++
			}
			for r < n-1 && r > i+2 && nums[r] == nums[r+1] {
				r--
			}
			if l >= r {
				break
			}
			s := e + nums[l] + nums[r]
			if s == target {
				return s
			} else if s < target {
				l++
			} else {
				r--
			}
			if abs(s-target) < abs(c-target) {
				c = s
			}
		}
	}
	return c
}
