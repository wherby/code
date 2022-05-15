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
        acc =0
        while lptr !=rptr:
            remove.append(self.span[lptr])
            lptr =lptr +1
        for item in remove:
            self.span.remove(item)
            if item.w ==0:
                acc += item.r-item.l+1
        node = Node(left,right,1)
        self.span.add(node)
        self.mergeNode(node)
        return acc
        
    def mergeNode(self,item):
        kptr = self.span.bisect_left(item)
        pre = kptr-1
        merged=[item]
        left,right= item.l,item.r
        while pre >0 and self.span[pre].w == item.w:
            merged.append(self.span[pre])
            left =self.span[pre].l
            pre =pre -1
        pst = kptr +1
        while pst < len(self.span) and self.span[pst].w == item.w:
            merged.append(self.span[pst])
            right = self.span[pst].r
            pst = pst+1
        for item in merged:
            self.span.remove(item)
        self.span.add(Node(left,right,item.w))
        
class CountIntervals(object):

    def __init__(self):
        self.cnt = 0
        self.sp = SpanNode()


    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        ac= self.sp.add(left,right)
        self.cnt += ac

    def count(self):
        """
        :rtype: int
        """
        return self.cnt


# re = CountIntervals()
# re.add(39,44)
# re.add(13,49)
# print(re.count())
# re.add(47,50)
# print(re.count())
# print(re.sp.span)

# re = CountIntervals()
# re.add(2,3)
# re.add(7,10)
# print(re.count())
# re.add(5,8)
# print(re.count())
# print(re.sp.span)

re = CountIntervals()
re.add(5,10)
print(re.count())
print(re.sp.span)
re.add(5,10)
print(re.count())
print(re.sp.span)