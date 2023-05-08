#https://cp-algorithms.com/data_structures/fenwick.html



class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)+1
        self.bit= [0]*self.n
        for i in range(1,self.n):
            self.add(i,arr[i-1])
    
    def sumTo(self, r):
        ret = 0
        while r >0:
            ret += self.bit[r]
            r -= r&(-r) # equal to [r&= r-1] https://www.bilibili.com/video/BV1Ez4y1Y7Az/
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx += idx&(-idx)
            

    
ls = [i for i in range(1,20)]
ft = FenwickTree(ls)
print(ft.bit)
last =0
for i in range(1,20):
    ft.add(i,2)
for i in range(1,20):
    t =ft.sumTo(i)
    print(ft.sumTo(i),t-last)
    last = t
