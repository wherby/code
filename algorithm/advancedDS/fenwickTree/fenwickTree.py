# https://leetcode-cn.com/problems/range-sum-query-mutable/submissions/
# Zero-index fenwick tree
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
            
arr= [i for i in range(1,10)]
ft = FenwickTree(arr)
print(ft.sumTo(4))
ft.add(1,10)
print(ft.sumTo(4))