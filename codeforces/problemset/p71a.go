package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d\n", &n)
	for i := 0; i < n; i++ {
		var word string
		fmt.Scanf("%s\n", &word)
		size := len(word)
		if size > 10 {
			fmt.Printf("%c%d%c\n", word[0], size-2, word[size-1])
			continue
		}
		fmt.Println(word)
	}
}
