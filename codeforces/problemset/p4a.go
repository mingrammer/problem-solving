package main

import (
	"fmt"
)

func main() {
	var w int64
	fmt.Scanf("%d", &w)
	if w > 2 && w%2 == 0 {
		fmt.Println("YES")
		return
	}
	fmt.Println("NO")
}
