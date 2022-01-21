# 合并链表，需要先求出链表的头节点，last记录了链表头节点a对应的链表的尾节点。
class DList():
    def __init__(self,ls):
        n = len(ls)
        self.ls = ls
        self.next = [0]*n
        self.last = [0]*n
        for i in range(n):
            self.next[i] =i
            self.last[i] = i
    
    def link(self,a,b):
        #print(a,b,dl.last,dl.next)
        self.next[self.last[a]] = b
        self.last[a] = self.last[b]
        #print(dl.last,dl.next)


dl = DList([1,2,3,4,5,6,7,8])
dl.link(0,1)
dl.link(0,2)
dl.link(0,3)
dl.link(0,4)
dl.link(0,5)
dl.link(0,6)
dl.link(0,7)
#dl.link(2,3)
#dl.link(1,2)
print(dl.last,dl.next)
# 0<-1
#         