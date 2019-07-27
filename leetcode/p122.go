package main

func maxProfit(prices []int) int {
	m := 0
	n := 1<<32 - 1
	pfs := 0
	for i, p := range prices {
		if i > 0 && p < prices[i-1] {
			n = 1<<32 - 1
			pfs += m
		}
		if p < n {
			n = p
			m = 0
		}
		pf := p - n
		if pf > m {
			m = pf
		}
	}
	pfs += m
	return pfs
}
