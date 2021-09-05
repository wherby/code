package main

import (
	"fmt"
)

func main() {
	var a =[]int{1}
	fmt.Println(a[:0])
	fmt.Println(a[:1])
	fmt.Println(a[1:])
	//fmt.Println(a[2:])  // this will fail
	fmt.Println("Hello, playground")
}
