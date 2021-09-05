package main2

import ("fmt"
"container/heap"
)

//for heap :https://golang.org/pkg/container/heap/

// An Item is something we manage in a priority queue.
type Item struct {
	value    int // The value of the item; arbitrary.
	priority int    // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
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
func (pq *PriorityQueue) update(item *Item, value int, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}

type Node struct{
	left,right int
	item *Item
}

type ExamRoom struct {
	pq *PriorityQueue
	caddMap map[int]*Node
}


func Constructor(N int) ExamRoom {
	var startItem = Item{0,N-1,0}
	var endItem = Item{N-1,N-1,1}
	var start = Node{-1,-1,&startItem}
	var end = Node{0,-1,&endItem}
	var map1 = make(map[int]*Node)
	map1[0] = &start
	map1[N-1] = &end
	pq := make(PriorityQueue, 2)

	pq[0] = &startItem
	pq[1] = &endItem
	heap.Init(&pq)
	var room = ExamRoom{&pq,map1}
	return room
}


func (this *ExamRoom) Seat() int {
	var c = heap.Pop(this.pq).(*Item)
	var point = this.caddMap[c.value]
	if point.left != -1{
		var value = (point.left + c.value)/2
		if value != point.left{
			var cadP = Item{value,value - point.left,0}
			heap.Push(this.pq,&cadP)
			var node = Node{point.left,c.value,&cadP}
			this.caddMap[value] = &node
		}
		this.caddMap[point.left].right = c.value
	}
	if point.right !=-1{
		var value = (point.right + c.value)/2
		if value != c.value{
			var cadP = Item{value,value - c.value,0}
			heap.Push(this.pq,&cadP)
			var node = Node{c.value,point.right,&cadP}
			this.caddMap[value] = &node
		}
		this.caddMap[point.right].left =c.value
	}
	return c.value
}


func (this *ExamRoom) Leave(p int)  {
		var node1 = this.caddMap[p]
		this.caddMap[node1.left].right =  node1.right
		this.caddMap[node1.right].left = node1.left
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
	fmt.Println(obj.Seat())
	obj.Leave(4)
	fmt.Println(obj.Seat())
}
