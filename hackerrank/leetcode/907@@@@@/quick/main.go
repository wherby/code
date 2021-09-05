package main
//https://leetcode.com/problems/sum-of-subarray-minimums
import ("fmt"
		"sort"
)

func sumSubarrayMins(A []int) int {
	type Node struct{
		left,right,value int
	}
	const CST = 1000000007
	var num = len(A)
	var minls = make([]Node, num)
	var sumls =make([]int, num)
	var re= 0
	var minIdex =1

	for i, v := range A{
		if i ==0{
			minls[i] = Node{0,0,v}
			sumls[i] =A[i]
			re = re + v
		}else{
			index := sort.Search(minIdex, func(j int) bool { return minls[j].value >= v })
			if(index == minIdex){
				minIdex = index+1
				minls[index] = Node{i,i,v}
				sumls[i] = sumls[i-1] +v
			}else{
				if index == 0{
					minls[0] = Node{0,i,v}
					sumls[i] = (i+1)*v
				}else{
					minls[index] = Node{minls[index-1].right+1,i,v}
					sumls[i] = sumls[minls[index-1].right] + v * (i- minls[index-1].right)
				}
				minIdex = index +1
			}
			re =re + sumls[i]
		}
	}
	return re %CST
}



func main() {
	var ls = []int{36,74,84,92,17,68,97,6,68,85}
	fmt.Println(sumSubarrayMins(ls))
}

