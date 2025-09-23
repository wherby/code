# 以i作为左端点，遍历取最大区间作为Seed，然后stack取最大值再遍历右端点
from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
from math import gcd 
class SparseTable:
    def __init__(self, data: list, func=gcd):
        self.func=func
        self.st=st=[list(data)]
        i,N=1,len(st[0])
        while 2*i<=N+1:
            qz=st[-1]
            st.append([func(qz[j],qz[j+i]) for j in range(N-2*i+1)])
            i<<=1
    def query(self, begin: int, end: int):
        lg=(end-begin+1).bit_length()-1
        return self.func(self.st[lg][begin], self.st[lg][end-(1<<lg)+1])

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k<=0 or n==0:
            return 0
        st_max=SparseTable(nums, max)
        st_min=SparseTable(nums, min)
        def diff(l,r):
            return st_max.query(l,r)-st_min.query(l,r)
        h=[]
        for l in range(n):
            heappush(h,(-diff(l,n-1),l,n-1))
        ans=0;cnt=0
        while cnt<k and h:
            v,l,r=heappop(h)
            v=-v
            ans+=v
            cnt+=1
            if r>l:
                r-=1
                heappush(h,(-diff(l,r),l,r))
        return ans