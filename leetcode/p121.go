package main

func maxProfit(prices []int) int {
	m := 0
	n := 1<<32 - 1
	for _, p := range prices {
		if p < n {
			n = p
		}
		pf := p - n
		if pf > m {
			m = pf
		}
	}
	return m
}
