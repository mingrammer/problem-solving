package main

func isToeplitzMatrix(matrix [][]int) bool {
	r, c := len(matrix), len(matrix[0])
	x := r - 1
	for x > 0 {
		x--
		n := matrix[x][0]
		for i := 0; i < r-x-1 && i < c-1; i++ {
			if n != matrix[x+i+1][i+1] {
				return false
			}
		}
	}
	y := 0
	for y < c-1 {
		y++
		n := matrix[0][y]
		for i := 0; i < c-y-1 && i < r-1; i++ {
			if n != matrix[i+1][y+i+1] {
				return false
			}
		}
	}
	return true
}
