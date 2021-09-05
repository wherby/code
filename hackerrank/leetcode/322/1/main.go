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

func coinChange(coins []int, amount int) int {
	MAXV :=1000000
	var GCD=1
	for _,x :=range coins{
		GCD = x*GCD
	}
	cnt := amount /GCD 
	quick := 0
	amountR := amount
	if cnt >1{
		amountR = amount %GCD  +GCD
		quick = (amount - amountR )/ maxLs(coins)
	}
	dp := make([]int,amountR+1)
	dp[0] =0
	for i:=1 ;i< amountR +1 ; i++{
		dp[i] = MAXV
		for j :=0;j< len(coins); j++{
			cv := coins[j]
			if i-cv >=0{
				tmp := dp[i-cv] +1
				if tmp < dp[i]{
					dp[i] = tmp
				}
			}
		}
	}
	if dp[amountR] >= MAXV{
		return -1
	}
	return dp[amountR] +quick
}

func main() {
	coins := []int{1}
	amount :=2
	fmt.Println(coinChange(coins,amount))
}