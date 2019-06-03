package main

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func expand(s string, l, r int) int {
	for l >= 0 && r < len(s) && s[l] == s[r] {
		l--
		r++
	}
	return r - l - 1
}

func longestPalindrome(s string) string {
	if len(s) < 1 {
		return ""
	}
	si, ei := 0, 0
	for i := 0; i < len(s); i++ {
		l1 := expand(s, i, i)
		l2 := expand(s, i, i+1)
		l := max(l1, l2)
		if l > ei-si {
			si = i - (l-1)/2
			ei = i + l/2
		}
	}
	return s[si : ei+1]
}
