package main

import (
	"math"
)

func minLen(strs []string) int {
	m := math.MaxInt32
	for _, s := range strs {
		l := len(s)
		if l < m {
			m = l
		}
	}
	return m
}

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	prefix := []byte{}
	for i := 0; i < minLen(strs); i++ {
		c := strs[0][i]
		for _, s := range strs {
			if c != s[i] {
				return string(prefix)
			}
		}
		prefix = append(prefix, c)
	}
	return string(prefix)
}
