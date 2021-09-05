package main

import ("fmt"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode {
    if len(nums) ==0{
		return nil
	}
	var idx =0
	maxV :=nums[0]
	for i:=0; i< len(nums); i++{
		if nums[i] > maxV{
			maxV = nums[i]
			idx = i
		}
	}

	root := TreeNode{nums[idx],constructMaximumBinaryTree(nums[:idx]),constructMaximumBinaryTree(nums[idx+1:])}
	return &root
}

func insertIntoMaxTree(root *TreeNode, val int) *TreeNode {
    if root == nil{
		return &TreeNode{val,nil,nil}
	}
	if root.Val< val{
		return &TreeNode{val,root,nil}
	}
	if root.Val > val{
		root.Right =insertIntoMaxTree(root.Right,val)
	}
	return root
}

func main() {
	nums := []int {3,2,1,6,0,5}
	fmt.Println(constructMaximumBinaryTree(nums))
}