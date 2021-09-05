package main

import ("fmt"
)
func clumsy(N int) int {
	var res = 0
	var tp =-1
	for i:= 0; i <N;i++{
		t := N-i
		if i%4 == 0{
			if i !=0{
				tp =1
			}
			tp =tp *-1  *t
		}
		if i%4 ==1{
			tp = tp *t
		}
		if i%4 ==2{
			tp = tp / t
			res = res + tp
			tp = 0
		}
		if i%4 ==3{
			res = res +t
		}
		if i==N-1{
			res = res + tp
		}
	}
	return res
}

func main() {
	fmt.Println(clumsy(4))
	fmt.Println("hello")
}