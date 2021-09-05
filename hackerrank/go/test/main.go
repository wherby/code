package main

import "fmt"



func reverse(x int) int {


	var re = 0
	for ; x !=0; {
		e := x%10
		x = x/10
		re = re *10 +e
	}
	if int(int32(re)) != re{
		return 0
	}
	return re
}

func main() {
	fmt.Println(reverse(-2147483648))
}