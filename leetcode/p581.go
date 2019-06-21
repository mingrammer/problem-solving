package main

func findUnsortedSubarray(nums []int) int {
	l, r, m := -1, -1, 0
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[m] {
			m = i
			continue
		}
		if nums[i] < nums[m] {
			if l == -1 {
				l = i - 1
			}
			for l > 0 && nums[l-1] > nums[i] {
				l--
			}
			r = i
		}
	}
	if l == -1 {
		return 0
	}
	return r - l + 1
}
