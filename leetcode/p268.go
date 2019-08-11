package main

func missingNumber(nums []int) int {
	sum := 0
	for _, n := range nums {
		sum += n
	}
	cnt := len(nums)
	return cnt*(cnt+1)/2 - sum
}
