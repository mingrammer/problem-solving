package main

import (
	"sort"
)

func threeSum(nums []int) [][]int {
	triplets := [][]int{}
	n := len(nums)
	if n < 3 {
		return triplets
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
			if s == 0 {
				triplets = append(triplets, []int{e, nums[l], nums[r]})
				l++
				r--
			} else if s < 0 {
				l++
			} else {
				r--
			}
		}
	}
	return triplets
}
