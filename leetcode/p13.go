package main

var table = map[byte]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

func romanToInt(s string) int {
	ri := 0
	n := len(s)
	for i := 0; i < n; i++ {
		v := table[s[i]]
		if i < n-1 {
			if table[s[i]] < table[s[i+1]] {
				v = table[s[i+1]] - table[s[i]]
				i++
			}
		}
		ri += v
	}
	return ri
}
