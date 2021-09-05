package main

import ("fmt"
"sort"
)
type TopVotedCandidate struct {
	times *[]int
	leaders *[]int
}


func Constructor(persons []int, times []int) TopVotedCandidate {
	var n = len(times)
	var dic1 = make([]int,n)
	var leaders = make([]int,n)
	var tmpLeader= 0
	var leader =-1
	for i,k := range persons{
		dic1[k]++
		if dic1[k] >= tmpLeader{
			tmpLeader = dic1[k]
			leader = k
		}
		leaders[i] =leader
	}
	var top = TopVotedCandidate{&times,&leaders}
	return top
}


func (this *TopVotedCandidate) Q(t int) int {
	var index = sort.Search(len(*this.times), func(i int) bool { return t <(*this.times)[i] })
	return (*this.leaders)[index-1]
}


func main() {
	var persons = []int{0,1,1,0,0,1,0}
	var times =[]int{0,5,10,15,20,25,30}
	var top = Constructor(persons,times)
	fmt.Println(top.Q(25))
	fmt.Println("hello")
}