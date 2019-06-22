package main

func peakIndexInMountainArray(A []int) int {
	var i int
	for ; i < len(A)-1; i++ {
		if A[i] > A[i+1] {
			break
		}
	}
	return i
}
