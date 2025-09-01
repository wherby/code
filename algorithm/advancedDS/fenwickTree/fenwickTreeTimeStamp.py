
#https://leetcode.cn/problems/sum-of-beautiful-subsequences/solutions/3768197/bei-shu-rong-chi-zhi-yu-shu-zhuang-shu-z-rs5w/
# Zero-index fenwick tree
class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        self.timestamp = 0
        self.time = [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
        
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            if self.time[r] == self.timestamp:
                ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            if self.time[idx] < self.timestamp:
                self.time[idx] = self.timestamp
                self.bit[idx] =0
            self.bit[idx] += delta
            idx =  idx | (idx +1)
    


            
arr= [i for i in range(1,10)]
ft = FenwickTree(arr)
print(ft.sumTo(4))
ft.add(1,10)
print(ft.sumTo(4))