package main

func singleNumber(nums []int) int {
	m := map[int]int{}
	for _, n := range nums {
		if _, ok := m[n]; !ok {
			m[n] = 0
		}
		m[n]++
	}
	for i, n := range m {
		if n == 1 {
			return i
		}
	}
	return 0
}
