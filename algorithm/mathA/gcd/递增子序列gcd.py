# https://leetcode.cn/problems/sum-of-beautiful-subsequences/description/
# 使用时间戳懒初始化

from typing import List, Tuple, Optional
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[{0}] {1}' .format( elapsed, name))
        return result
    return clocked
@clock
def getAllDivN(MAX):
    MAX = MAX +1
    fac = [[] for _ in range(MAX)]
    for i in range(1,MAX):
        for j in range(i,MAX,i):
            fac[j].append(i)
    return fac 


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
DList = getAllDivN(70001)
class Solution:
    @clock
    def totalBeauty(self, nums: List[int]) -> int:
        mod = 10**9+7
        mx = max(nums)
        gp = [[] for _ in range(mx+1)]
        for a in nums:
            for b in DList[a]:
                gp[b].append(a)
        f = [0]*(mx+1)
        ftree = FenwickTree([0]*(mx+1))
        def count_subSeq(blist):
            ftree.timestamp+=1
            res = 0
            for a in blist:
                cnt = ftree.sumTo(a-1) +1
                res +=cnt 
                ftree.add(a,cnt)
            return res
        ans = 0
        for a in range(mx,0,-1):
            f[a] = count_subSeq(gp[a])
            for j in range(a*2,mx+1,a):
                f[a] -=f[j]
            ans += a*f[a]
        return ans%mod


from input import nums
re = Solution().totalBeauty(nums )
print(re)