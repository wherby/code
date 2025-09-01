
# https://leetcode.cn/problems/sum-of-beautiful-subsequences/solutions/3768197/bei-shu-rong-chi-zhi-yu-shu-zhuang-shu-z-rs5w/


class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)+1
        self.bit= [0]*self.n
        self.timestamp = 0
        self.time = [0]*self.n
        for i in range(1,self.n):
            self.add(i,arr[i-1])
    
    def sumTo(self, r):
        ret = 0
        while r >0:
            if self.time[r] == self.timestamp:
                ret += self.bit[r]
            r -= r&(-r) # equal to [r&= r-1] https://www.bilibili.com/video/BV1Ez4y1Y7Az/
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            if self.time[idx] < self.timestamp:
                self.time[idx] = self.timestamp
                self.bit[idx] = 0
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
