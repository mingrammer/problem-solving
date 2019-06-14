package main

func checkPossibility(nums []int) bool {
	c := 1
	for i := 0; i < len(nums)-1; i++ {
		if c < 0 {
			return false
		}
		if nums[i] <= nums[i+1] {
			continue
		}
		if i > 0 && nums[i+1] < nums[i-1] {
			nums[i+1] = nums[i]
		} else {
			nums[i] = nums[i+1]
		}
		c--
	}
	if c < 0 {
		return false
	}
	return true
}
