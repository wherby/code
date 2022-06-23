# https://cp-algorithms.com/data_structures/fenwick.html
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
            r -= r&(-r)
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx += idx&(-idx)
    
    def range_add(self,l,r,val):
        self.add(l,val)
        self.add(r+1,-val)

ls = [0 for i in range(1,20)]
ft = FenwickTree(ls)
ft.range_add(2,10,20)
ft.range_add(3,14,10)
for i in range(1,20):
    print(ft.sumTo(i))
