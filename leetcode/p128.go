package main

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// use sorting.
// func longestConsecutive(nums []int) int {
// 	if len(nums) < 1 {
// 		return 0
// 	}
// 	sort.Ints(nums)
// 	m, n := 1, 1
// 	for i := 0; i < len(nums)-1; i++ {
// 		if nums[i+1] == nums[i] {
// 			continue
// 		}
// 		if nums[i+1] == nums[i]+1 {
// 			m++
// 			continue
// 		}
// 		n = max(n, m)
// 		m = 1
// 	}
// 	n = max(n, m)
// 	return n
// }

// use a map.
func longestConsecutive(nums []int) int {
	if len(nums) < 1 {
		return 0
	}
	cm := make(map[int]bool)
	for _, n := range nums {
		cm[n] = false
	}
	m, n := 1, 1
	for k, v := range cm {
		if v {
			continue
		}
		l := k - 1
		for {
			_, ok := cm[l]
			if !ok {
				break
			}
			cm[l] = true
			l--
			m++
		}
		r := k + 1
		for {
			_, ok := cm[r]
			if !ok {
				break
			}
			cm[r] = true
			r++
			m++
		}
		n = max(n, m)
		m = 1
	}
	n = max(n, m)
	return n
}
