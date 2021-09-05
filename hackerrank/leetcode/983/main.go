package main

import ("fmt"
)

func maxLs(ls []int) int{
	var maxV = ls[0]
	for _,v := range ls{
		if v >maxV{
			maxV = v
		}
	}
	return maxV
}
func minLs(ls []int) int{
	var minV = ls[0]
	for _,v := range ls{
		if v <minV{
			minV = v
		}
	}
	return minV
}

func mincostTickets(days []int, costs []int) int {
	var dp =make([]int,396)
	for i:=0;i<31;i++{
		dp[i]=0
	}
	var dic1 = make(map[int]bool)
	for _,x :=range days{
		dic1[x] = true
	}
	for i:=1; i< 366;i++{
		k :=i+30
		if _,ok:=dic1[i];ok{
			d1 := dp[k-1] +costs[0]
			d2 := dp[k-7] + costs[1]
			d3 := dp[k-30] + costs[2]
			dp[k] = minLs([]int{d1,d2,d3})
		}else{
			dp[k] = dp[k-1]
		}
	}
	return dp[395]
}


func main() {
	var days = []int{1,4,6,7,8,20}
	var costs = []int{2,7,15}
	fmt.Println(mincostTickets(days,costs))
}
