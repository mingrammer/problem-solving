package main

import "fmt"

func swap(nums []int, i, j int) {
	t := nums[i]
	nums[i] = nums[j]
	nums[j] = t
}

// use an additional array. more faster than in-place.
// func rotate(nums []int, k int) {
// 	n := len(nums)
// 	orig := make([]int, n)
// 	copy(orig, nums)
// 	for i := 0; i < n; i++ {
// 		nums[(i+k)%n] = orig[i]
// 	}
// 	fmt.Println(nums)
// }

// in-place. do not require an additional memory space.
// func rotate(nums []int, k int) {
// 	n := len(nums)
// 	for i := 0; i < k%n; i++ {
// 		for j := n - 1; j > 0; j-- {
// 			swap(nums, j, j-1)
// 		}
// 	}
// 	fmt.Println(nums)
// }

// in-place with reverse. do not require an additional memory space and fast.
func rotate(nums []int, k int) {
	n := len(nums)
	k = k % n
	for i := 0; i < n/2; i++ {
		swap(nums, i, n-1-i)
	}
	for i := 0; i < k/2; i++ {
		swap(nums, i, k-1-i)
	}
	for i := k; i < (n+k)/2; i++ {
		swap(nums, i, n+k-1-i)
	}
	fmt.Println(nums)
}
