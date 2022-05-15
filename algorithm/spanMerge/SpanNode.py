# This will have timeout issue for not merge node
from sortedcontainers import SortedList
from bisect import bisect_right,bisect_left
class Node:
    def __init__(self,l,r,w):
        self.l =l
        self.r =r
        self.w =w 
    
    def __ge__(self,other):
        return (self.l,self.r,self.w) >(other.l,other.r,other.w)
    
    def __lt__(self,other):
        return (self.l,self.r,self.w) <(other.l,other.r,other.w)
    def __str__(self):
        return "({0},{1},{2})".format(self.l,self.r,self.w)
    def __repr__(self):
        return "({0},{1},{2})".format(self.l,self.r,self.w)

class SpanNode:
    def __init__(self):
        self.span = SortedList([Node(-1,10**10,0)])
    
    def splitAt(self,x):
        idx = bisect_left(self.span,Node(x,x,-1))-1
        if self.span[idx].l == x: return idx 
        node = Node(x,self.span[idx].r,self.span[idx].w)
        self.span[idx].r = x-1
        self.span.add(node)
        return idx+1
        
    def add(self,left,right):
        lptr = self.splitAt(left)
        rptr = self.splitAt(right+1)
        remove =[]
        while lptr !=rptr:
            remove.append(self.span[lptr])
            lptr =lptr +1
        for item in remove:
            self.span.remove(item)
        self.span.add(Node(left,right,1))
        

spn = SpanNode()
print(spn.span)
spn.add(2,3)
print(spn.span)
spn.add(7,10)
spn.add(5,8)
print(spn.span)
        