package main

import ("fmt"
	"os"
	 "bufio"
	 "container/list"
	 "strconv"
	 "strings"
	 )

type Tree struct{
	Value int
	Left *Tree
	Right *Tree
}

type PersistentArray struct{
	LastUsed int
	Pool []Tree
	L int 
	R int
}

func(array *PersistentArray) GetNewNode() *Tree {
	var lastused = array.LastUsed
	array.LastUsed += 1
	return &array.Pool[lastused]
}

func(array *PersistentArray) get(v *Tree ,l int,r int, at int) int{
	if(v == nil){
		return 0
	}

	if(l +1 == r){
		return v.Value
	}

	var m = (l + r)/2

	if(at < m){
		return array.get(v.Left,l,m,at)
	}else{
		return array.get(v.Right,m,r,at)
	}
}

func(array *PersistentArray) upd(v *Tree,l int,r int, at int, val int) *Tree{
	var res = array.GetNewNode()
	
	if( v != nil){
		*res = *v
	}

	if( l +1 == r){
		res.Value = val
		return res
	}

	var m =( l + r )/2

	if (at < m){
		res.Left = array.upd(res.Left,l,m,at,val)
	}else{
		res.Right = array.upd(res.Right,m,r,at,val)
	}
	return res
}

// func test(){
// 	var pool []Tree = make([]Tree, 20000000)
// 	var array = &PersistentArray{0,pool,0,10}
// 	var L =0
// 	var R = 10
// 	var version []*Tree = make([]*Tree, 10)
// 	var root = array.GetNewNode()
// 	for i:=0; i< 10; i +=1{
// 		root =array.upd(root,L,R,i,i)
// 		version[i] = root
// 		for j :=0; j<10; j+=1{
// 			fmt.Print(array.get(root,L,R,j))
// 			fmt.Print(" ")
// 		}
// 		fmt.Println()
// 	}
// }

func main() {
	file,_:= os.Open("./input/input00.txt")

	defer file.Close()

	scaner := bufio.NewScanner(file)
	//scaner2 := bufio.NewScanner(os.Stdin)
	ls := list.New()
	for(scaner.Scan()){
		ls.PushBack(scaner.Text())
	}

	var index = ls.Front()
	n,_:= strconv.Atoi(index.Value.(string))
	ans := make([]int,n)
	index = index.Next()
	m :=0

	var pool []Tree = make([]Tree, 20000000)
	var array = &PersistentArray{0,pool,0,1000000}
	var L =0
	var R = 1000000
	var version []*Tree = make([]*Tree, n)
	for i :=0; i <n ;i ++{
		ins:= strings.Split(index.Value.(string)," ")
		index= index.Next()
		if ins[0] =="-"{
			m--
		}else{
			x,_:= strconv.Atoi(ins[1])
			x= x-1
			if m == 0{
				version[m] =array.upd(nil,L,R,x,1)
			}else{
				j:=ans[m-1]
				version[m] = array.upd(version[j],L,R,x,m+1)
				ans[m] = array.get(version[j],L,R,x) 			
			}
			m++
		}
		if(m >0){
			fmt.Println(ans[m-1])
		}else{
			fmt.Println(0)
		}
	}

}