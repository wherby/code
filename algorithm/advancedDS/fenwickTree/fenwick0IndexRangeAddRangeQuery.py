class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx =  idx | (idx +1)
            
class RangeFenwick:
    def __init__(self,arr) :
        self.n = len(arr)
        self.B1 = FenwickTree([0]*self.n)
        self.B2 = FenwickTree([0]*self.n)
        for i,a in enumerate(arr):
            self.range_add(i+1,i+1,a)
        
    def range_add(self,l,r,x):
        self.B1.add(l,x)
        self.B1.add(r+1,-x)
        self.B2.add(l, x*(l-1))
        self.B2.add(r+1,-x*r)
    
    def sum(self, idx):
        re = self.B1.sumTo(idx)*idx - self.B2.sumTo(idx)
        return re
    
ls = [i+1 for i in range(20)]
ft2d = RangeFenwick(ls)
ft2d.range_add(1,10,10)
print(ft2d.B1.bit,ft2d.B2.bit)
print(ft2d.sum(4))
print(ft2d.sum(19))