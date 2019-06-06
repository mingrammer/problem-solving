package main

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func convert(s string, numRows int) string {
	if numRows < 2 {
		return s
	}
	n := len(s)
	z := make([][]byte, 0)
	j := 0
	for i := 0; i < n; i++ {
		z = append(z, make([]byte, numRows))
		if i%2 == 0 {
			for k := 0; k < min(numRows, n-j); k++ {
				z[i][k] = s[j+k]
			}
			j += numRows
		} else {
			limit := (numRows - 2) - (n - j)
			for k := numRows - 2; k > max(0, limit); k-- {
				z[i][k] = s[j]
				j++
			}
		}
		if j > n-1 {
			break
		}
	}
	cs := []byte{}
	for r := 0; r < numRows; r++ {
		for c := 0; c < len(z); c++ {
			v := z[c][r]
			if v > 0 {
				cs = append(cs, v)
			}
		}
	}
	return string(cs)
}
