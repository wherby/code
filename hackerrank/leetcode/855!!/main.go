package main

import ("fmt"
"container/heap"
)

//for heap :https://golang.org/pkg/container/heap/
type Node struct{
	left,right int
	valid bool
}
// An Item is something we manage in a priority queue.
type Item struct {
	value    *Node // The value of the item; arbitrary.
	priority int    // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	if pq[i].priority==pq[j].priority {
		return pq[i].value.left < pq[j].value.left
	}
	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Item, value *Node, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}



type ExamRoom struct {
	count int
	pq *PriorityQueue
	cadFirst,cadLast map[int]*Item
}

func (this *ExamRoom)put_node(node Node){
	var priority =0
	if node.left ==0 || node.right == this.count-1{
		priority = node.right - node.left
	}else{
		priority = (node.right - node.left) /2
	}
	var item = Item{&node, priority,0}
	this.cadFirst[node.left] = &item
	this.cadLast[node.right] = &item
	heap.Push(this.pq,&item)
}

func Constructor(N int) ExamRoom {
	var cadFirst = make(map[int]*Item)
	var cadLast = make(map[int]*Item)
	pq := make(PriorityQueue, 0)
	room := ExamRoom{N,&pq,cadFirst,cadLast}
	room.put_node(Node{0,N-1,true})
	return room
}


func (this *ExamRoom) Seat() int {
	var p = heap.Pop(this.pq).(*Item).value
	for {
		if p.valid == true{
			delete(this.cadFirst,p.left)
			delete(this.cadLast,p.right)
			break
		}
		p = heap.Pop(this.pq).(*Item).value
	}
	

	var ret =0
	if p.left ==0{
		ret = 0
		if p.left != p.right{
			this.put_node(Node{p.left+1, p.right,true})
		}
	}else if p.right ==this.count-1{
		ret = this.count -1
		if p.left != p.right{
			this.put_node(Node{p.left, p.right-1,true})
		}
	}else{
	  //fmt.Println(p)
		ret = (p.left +p.right) /2
		if ret > p.left{
			this.put_node(Node{p.left,ret-1,true})
		}
		if ret < p.right {
			this.put_node(Node{ret+1, p.right,true})
		}
	}
	return ret
}



func (this *ExamRoom) Leave(p int)  {
	var first =p
	var last =p
	var left = p -1
	var right = p+1
	if left >=0 {
		if val,ok:=this.cadLast[left];ok{
			val.value.valid = false
			first = val.value.left
		}
	}
	if right<this.count {
		if val,ok := this.cadFirst[right]; ok{
			val.value.valid = false
			last =val.value.right
		}
	}
	//fmt.Println(Node{first,last,true})
	this.put_node(Node{first,last,true})
}


/**
 * Your ExamRoom object will be instantiated and called as such:
 * obj := Constructor(N);
 * param_1 := obj.Seat();
 * obj.Leave(p);
 */


 
func main() {
	var obj = Constructor(10)
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	obj.Leave(0)
	obj.Leave(4)
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
	fmt.Println(obj.Seat())
}
