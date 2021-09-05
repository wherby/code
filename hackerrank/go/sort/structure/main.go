package main

import (
    "fmt"
    "sort"
)

type Node struct{
	left,right,value int
}

func main() {
    a := []int{1, 3, 6, 10, 15, 21, 28, 36, 45, 55}
	x := 60
	num :=len(a)
	b := make([]Node, num)
	for i,v := range a{
		b[i].left = i
		b[i].right = i
		b[i].value =v
	}

    i := sort.Search(len(a), func(i int) bool { return b[i].value >= x })
    if i < len(b) && b[i].value == x {
        fmt.Printf("found %d at index %d in %v\n", x, i, b)
    } else {
        fmt.Printf("%d not found in %v\n", x, b)
	}
	fmt.Print(i)
}