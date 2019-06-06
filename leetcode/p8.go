package main

import (
	"math"
)

func myAtoi(str string) int {
	p := []rune{}
	for _, c := range str {
		if c == ' ' {
			if len(p) > 0 {
				break
			}
		} else if c == '+' || c == '-' {
			if len(p) > 0 {
				break
			}
			p = append(p, c)
		} else if c > 47 && c < 58 {
			p = append(p, c)
		} else {
			break
		}
	}
	if len(p) == 0 {
		return 0
	}
	var neg bool
	switch p[0] {
	case '-':
		neg = true
		fallthrough
	case '+':
		p = p[1:]
	}
	x := 0
	for _, r := range p {
		x = x*10 + int(r-48)
		if !neg && x > math.MaxInt32 {
			return math.MaxInt32
		}
		if neg && x > math.MaxInt32 {
			return math.MinInt32
		}
	}
	if neg {
		x = -x
	}
	return x
}
