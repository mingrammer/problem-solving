package main

import (
	"math"
)

var minS [][]int

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func _minScoreTriangulation(A []int, i, j int) int {
	if j-i < 2 {
		return 0
	}
	if minS[i][j] > 0 {
		return minS[i][j]
	}
	m := math.MaxInt32
	for k := i + 1; k < j; k++ {
		l := _minScoreTriangulation(A, i, k)
		r := _minScoreTriangulation(A, k, j)
		m = min(m, l+(A[i]*A[k]*A[j])+r)
	}
	minS[i][j] = m
	return m
}

func minScoreTriangulation(A []int) int {
	l := len(A)
	minS = make([][]int, l)
	for i := 0; i < l; i++ {
		minS[i] = make([]int, l)
	}
	return _minScoreTriangulation(A, 0, len(A)-1)
}
