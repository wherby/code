package main

import "fmt"

func main() {
	var nowhere *string
	fmt.Println(nowhere)
	//fmt.Println(*nowhere)
	var v interface{}
	fmt.Printf("%T %v %v\n", v, v, v == nil)
	var p *int
	v = p
	fmt.Printf("%T %v %v\n", v, v, v == nil)
	fmt.Printf("%#v\n", v)
}
