package main

import ("fmt"
		"sort"
)

func sumSubarrayMins(A []int) int {
	const CST = 1000000007
	var num = len(A)
	var minls = make([]int, num)
	var sumls =make([]int, num)
	var re= 0
	for i, v := range A{
		if i ==0{
			minls[i] = v
			sumls[i] =A[i]
			re = re + v
		}else{
			minls[i] =v
			sumls[i] = sumls[i-1] +v
			index := sort.Search(i, func(j int) bool { return minls[j] >= v })
			for j:=index;j<=i;j++{
				minls[j] = v
				if j>0 {
					sumls[j] = sumls[j-1] +v
				}else{
					sumls[0] =v
				}
			}
			re =re + sumls[i]
		}
	}
	return re %CST
}



func main() {
	var ls = []int{3,1,2,4}
	fmt.Println(sumSubarrayMins(ls))
}

