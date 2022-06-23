import random
# ./pic/fenwickUsage.png  reverse pair counting
# When the value of scope is limited for list
# Zero-indexed
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
            
ls = [random.randint(0,100) for i in range(10000)]
fw= FenwickTree([0]*101)  # value of scope of ls is 0-100

for i,a in enumerate(ls):
    k = fw.sumTo(a-1)
    fw.add(a,1)
    print(k) # K is the number of value which is less than a when j <i