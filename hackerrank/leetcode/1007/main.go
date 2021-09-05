package main

import ("fmt"
)

func minDominoRotations(A []int, B []int) int {
	var dic = make(map[int]int,6)
	for _,n := range A{
		dic[n]++
	}
	for _,n := range B{
		dic[n]++
	}
	var maxV = 0
	var maxN = -1
	for k,v := range dic{
		if maxV <v{
			maxV =v
			maxN = k
		}
	}
	var aN =0
	var bN =0
	for i,n:= range A{
		if n != maxN &&  B[i] !=maxN{
			return -1
		}
		if n ==maxN && B[i] != maxN{
			bN++
		}
		if n != maxN && B[i] == maxN{
			aN ++
		}
	}
	if aN > bN{
		return bN
	}else{
		return aN
	}
}
func main() {
	var A= []int{2,1,2,4,2,2}
	var B=[]int{5,2,6,2,3,2}
	fmt.Println(minDominoRotations(A,B))
	fmt.Println("hello")
}