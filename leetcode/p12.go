package main

var (
	table = map[int]int{
		1:    0,
		5:    1,
		10:   2,
		50:   3,
		100:  4,
		500:  5,
		1000: 6,
	}
	symbols = []byte{'I', 'V', 'X', 'L', 'C', 'D', 'M'}
)

func romanUnit(u, n int) []byte {
	bs := []byte{}
	switch n {
	case 4:
		bs = []byte{symbols[table[u]], symbols[table[u]+1]}
	case 9:
		bs = []byte{symbols[table[u]], symbols[table[u]+2]}
	default:
		if n >= 5 {
			bs = append(bs, symbols[table[u]+1])
		}
		for i := 0; i < n%5; i++ {
			bs = append(bs, symbols[table[u]])
		}
	}
	return bs
}

func intToRoman(num int) string {
	units := []int{1000, 100, 10, 1}
	roman := []byte{}
	for _, v := range units {
		roman = append(roman, romanUnit(v, num/v)...)
		num %= v
	}
	return string(roman)
}
