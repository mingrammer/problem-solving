package main

func lengthOfLongestSubstring(s string) int {
	ans := 0
	m := map[byte]bool{}
	for i, _ := range []byte(s) {
		for _, d := range []byte(s[i:]) {
			if _, ok := m[d]; ok {
				break
			}
			m[d] = true
		}
		if len(m) > ans {
			ans = len(m)
		}
		m = map[byte]bool{}
	}
	return ans
}
