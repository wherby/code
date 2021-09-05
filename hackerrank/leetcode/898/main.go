package main

import ("fmt"
)

func subarrayBitwiseORs(A []int) int {
	var allSet = map[int]bool{}
	var cur =map[int]bool{}
	for _,v := range A{
		var cur2 =map[int]bool{}	
		cur2[v]=true
		for k,_ :=range cur{
			v1 := v| k
			cur2[v1] = true
			allSet[v1] =true
		}
		allSet[v] = true
		cur = cur2
	}
	return len(allSet)
}



func main() {
	var ls = []int{1,2,4}
	fmt.Println(subarrayBitwiseORs(ls))
}

