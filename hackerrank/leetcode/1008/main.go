package main

import ("fmt"
"sort"
)

type TreeNode struct {
	     Val int
	     Left *TreeNode
	     Right *TreeNode
	 }

func bstFromPreorder(preorder []int) *TreeNode {
	if len(preorder) == 0{
		return nil
	}
	var leftEnd = sort.Search(len(preorder), func(i int) bool { return preorder[i] > preorder[0] })
	var leftNode = bstFromPreorder(preorder[1:leftEnd])
	var rightNode = bstFromPreorder(preorder[leftEnd:])
	var root = TreeNode{preorder[0],leftNode,rightNode}
	return &root
}

func printTree(root *TreeNode) {
	if root == nil{
		return
	}
	fmt.Println(root.Val)
	printTree(root.Left)
	printTree(root.Right)
}

func main() {
	var preorder = []int{8,5,1,7,10,12}
	var root= bstFromPreorder(preorder)
	printTree(root)
	fmt.Println("hello")
}