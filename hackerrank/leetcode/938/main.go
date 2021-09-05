package main

import ("fmt"
)

 type TreeNode struct {
	     Val int
	     Left *TreeNode
	     Right *TreeNode
	 }


func rangeSumBST(root *TreeNode, L int, R int) int {
	var re =0
	if root == nil{
		re= 0
	}
	if root.Val >=L && root.Val <= R{
		re= root.Val + rangeSumBST(root.Left ,L,R) + rangeSumBST(root.Right, L,R)
	}
	if root.Val <L{
		re = rangeSumBST(root.Right,L,R)
	}
	if root.Val >R{
		re= rangeSumBST(root.Left, L,R)
	}
	return re
}



func main() {

	fmt.Println("hello")
}