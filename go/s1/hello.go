package main

import (
	"fmt"
	"os"
)

func main() {
	var s, seq string
	var numbers = [5]int{1, 2, 3, 4, 5}
	for i := 1; i < len(os.Args); i++ {
		s += seq + os.Args[i]
		seq = " "
	}

	s1 := numbers[2:5]
	numbers[4] = 11
	s2 := append(s1, 8)
	numbers[3] = 12
	fmt.Println(s)
	fmt.Println(numbers, s1, s2)
}
